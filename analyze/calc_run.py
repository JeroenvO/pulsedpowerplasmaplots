"""
Convert all output of a measurement to a pickle and xlsx file. These files can be used for plotting data.

Parse log excel file
Get ozone concentration
Get scope plots

Ocean optics HR2000 -> SpectraSuite -> CSV -> spectrum_parse.{a,b,c} ↴
LeCroy WaveAce 224 -> EasyScope 	-> CSV -> scope_parse.{a,b,c,d}  ↴
Manual written log 					-> XLSX -> calc_run.py			-|-> data.pkl & data.xlsx

Make list of dicts. Each dict is one measurement and contains all relevant input and output values.
Jeroen van Oorschot 2017-2018, Eindhoven University of Technology
jeroen@jjvanoorschot.nl
"""
import os
import pickle

import numpy as np
from openpyxl.reader.excel import load_workbook, Workbook

from analyze.scope_parse.c_get_lines import get_vol_cur_single, get_vol_cur_multiple
from analyze.scope_parse.d_calc import calc_output
from analyze.spectrum_parse.c_concentration import ozone_concentration, ozone_ppm
from visualize.helpers.helpers import sort_data

# defines, (usages see bottom of script)
long_meas_len = 0.111
short_meas_len = 0.03
reactor_glass_long = 14e-12  # long glass reactor capacitance
reactor_glass_short = 6.2e-12  # short glass reactor capacitance
reactor_glass_short_quad = 9e-12  # short glass reactor capacitance with four small electrodes parallel
reactor_ceramic = 391e-12
reactor_alixpress = 161e-12

# Folder with measuremtn. Folder has to contain:
# * log.txt
# * spect/m00000.txt  with spectral data
# * scope/000.csv with 000=used input voltage
# See bottom of file for run params.


def calc_run(run_dir,
             react_cap,
             spect_dir='spect',
             scope_dir='scope',
             scope_multiple = False,
             log_file='log.xlsx',
             scope_file_name_index=0,
             meas=short_meas_len):
    """
    Calculate all parameters for one measure run. Output to a pickle and xlsx file.

    :param run_dir: Directory with log file and directories for scope and spectra data.
    :param react_cap: capacitance of the used reactor in F.
    :param spect_dir: subdirectory with the spectra data.
    :param scope_dir: subdirectory with the scope data
    :param log_file: name of the logfile with input parameters [voltage, freq, v18,9ohm input, spectfile, Temp, airflow]
    :param scope_file_name_index: column of log_file that is used for the scope filenames, 0=volt, 1=freq, 2=pulsew
    :param meas: lenght of the measure cell
    :return: none
    """
    if log_file not in os.listdir(run_dir):
        return
    assert spect_dir in os.listdir(run_dir)
    assert scope_dir in os.listdir(run_dir)
    # Get ozone concentrations:
    all_ozone = ozone_concentration(path_name=run_dir + spect_dir, opt_path=meas)
    all_ppm = ozone_ppm(all_ozone)

    # assuming format: voltage, freq, voltage on 18,9ohm input, meting spect, Temp, airflow
    log_file = run_dir + '/' + log_file
    resistor_val = 18.9  # resistance of measure resistor for input current

    sheet = load_workbook(filename=log_file, read_only=True).active
    data = []
    for row in sheet.iter_rows(min_row=2):
        data_row = []
        for cell in row[0:7]:
            # read values from workbook
            data_row.append(cell.value)

        if all([not data for data in data_row]):  # if line is all empty
            print('finished reading')
            break
        if None in data_row:
            print("Error! Some empty cells found in: " + str(data_row))
        # 0: voltage        [V]
        # 1: freq           [Hz]
        # 2: duration       [us]
        # 3: v18, 9ohm input[V]
        # 4: spectfile      [filename]
        # 5: Temp           [deg. Cels.]
        # 6: airflow        [ls/min]
        I = data_row[3] / resistor_val  # generator input current [A]
        P = I * data_row[0]  # generator input power [W]
        Pk = P / 3.6e6  # input power in kWh/s
        iEp = P / data_row[1]  # input energy per pulse [J]
        # iEpk = iEp / 1000 * 3600  # input energy per pulse {kWh]
        co3 = all_ozone[data_row[4]]  # mol/m3
        co3g = co3 * 48  # gram/m3 o3
        lss = data_row[6] / 60  # liter air per second
        m3s = lss / 1000  # ls/min/1000/60=m3/s
        o3f = co3g * m3s  # (gram/m3)*(m3/s)=gram/second o3

        # get output waveforms
        dic = {}
        try:
            if scope_multiple:
                lines = get_vol_cur_multiple(run_dir + scope_dir + '/' + str(data_row[scope_file_name_index]))
            else:
                line = get_vol_cur_single(run_dir + scope_dir + '/' + str(data_row[scope_file_name_index]))
            output_time, output_v, output_i = line
            # check scaling of current waveform
            assert 2 <= max(output_i) < 30  # max current between 2A and 30A
            # calculate output parameters from d_calc.py and append them to the dict with prepend '_output'
            for key, val in calc_output(line, react_cap=react_cap, gen_res_high=225, gen_res_low=50).items():
                dic['output_' + key] = val
            # output power on plasma [Watt], compensated for capacitance
            output_p_plasma = (dic['output_e_plasma'] * data_row[1])
        except IOError:
            output_time = output_v = output_i = output_p_plasma = 0
            line = None

        dic = {**dic,
               # manually noted values (inputs)
               'input_v': data_row[0],  # input voltage in V
               'input_v_output': data_row[0] * 15,  # excpected output voltage of generator
               'input_f': data_row[1],  # pulse frequency in Hz
               'input_l': data_row[2],  # pulse length in us.
               'temperature': data_row[5] or 22,  # temperature in deg Celsius, default to 22
               'airflow_lm': data_row[6],  # airflow in ls/min
               'airflow_ls': lss,  # airflow in ls/s
               'airflow_m3s': m3s,  # airflow in m3/s

               # calculated values from noted values. (This is not compensated for resistive losses in generator!!)
               'input_c': I,  # input current to generator
               'input_p': P,  # input power to generator
               'input_pulse_energy': iEp,  # input energy per pulse in Joule
               'input_energy_dens': P / lss,  # input energy to generator in Joule/ Liter used air

               # values from ozone spectrum, as obtained from spectrometer.
               'o3_gramm3': co3g,
               'o3_molm3': co3,  # o3 concentration in Mol/m3
               'o3_ppm': all_ppm[data_row[4]],  # o3 concentration in ppm
               'o3_gramsec': o3f,  # o3 production in gram/second

               # scope spectra
               'output_t': output_time,
               'output_v': output_v,
               'output_c': output_i,

               # o3 generation efficiency
               'input_yield_gj': o3f / P,  # efficiency in gram/Joule
               'input_yield_gkwh': o3f / Pk,  # efficiency in gram/kWh
               'output_p_avg': output_p_plasma,
               'output_energy_dens': output_p_plasma / lss,
               'output_yield_gj': o3f / output_p_plasma,
               'output_yield_gkwh': o3f / (output_p_plasma / 3.6e6),
               }

        # add this measurement to the total list.
        data.append(dic)

    # sort data
    if scope_file_name_index == 0:
        data = sort_data(data, 'input_v')
    elif scope_file_name_index == 1:
        data = sort_data(data, 'input_f')
    elif scope_file_name_index == 2:
        data = sort_data(data, 'input_l')
    else:
        raise Exception

    # save pickle
    with open(run_dir + '/data.pkl', 'wb') as f:
        pickle.dump(data, f, )

    # save xlsx
    wb = Workbook()
    ws = wb.active
    ws.title = "data"
    # make header row.
    # row 5 probably contains all headers, since the first few will miss some as they are reference lines.
    keys = []

    for key, value in sorted(data[4].items()):
        # don't save arrays of values, it is too much information
        try:
            value = float(value)
            if not np.isfinite(value):  # replace inf and -inf with 0
                continue
        except:
            # skip columns with arrays as value.
            continue
        keys.append(key)
    ws.append(keys)

    # fill data for all keys
    for meas in data:
        row = []
        for key in keys:
            try:
                value = meas[key]
                if not np.isfinite(value):  # replace inf and -inf with 0
                    value = 0
            except:
                value = 0
            row.append(value)
        ws.append(row)
    # make unique filename because excel cannot open multiple workbooks with the same name
    file_name = '-'.join(run_dir.split('/')[-3:])
    wb.save(filename=run_dir + '/' + file_name + '.xlsx')

    print("finished writing")
    return 1


# path = "G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500hz/" # directory with subdirectories with measurements
# path = "G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500hz/"  # directory with subdirectories with measurements
# path = "G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/"  # directory with subdirectories with measurements
path = "G:/Prive/MIJN-Documenten/TU/62-Stage/20180103-1000Hz/"  # directory with subdirectories with measurements
### to run dir with subdirs:
dirs = os.listdir(path)
### to run one dir
# dirs = ['run1-1us']
# length of used measure cell
meas_len = short_meas_len
# capacitance of used reactor
react_cap = reactor_glass_long  # reactor_glass_short_quad
# which column of log.xlsx contains the filename for scope. 0=volt, 1=freq, 2=pulsew
scope_file_name_index = 0
# whether multiple scope spectra are stored for each measurement. If true, save as xxx_y.csv with y as index number
scope_multiple = False
for dir in dirs:
    run_dir = path + dir + '/'
    if os.path.isdir(run_dir):
        print(run_dir)
        # scope_file_name_index which column of log.xlsx contains the filename for scope.
        # 0=volt, 1=freq, 2=pulsew
        calc_run(run_dir, meas=meas_len, scope_file_name_index=scope_file_name_index, scope_multiple=scope_multiple, react_cap=react_cap)
