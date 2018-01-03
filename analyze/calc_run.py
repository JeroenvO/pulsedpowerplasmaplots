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
import pickle

import numpy as np
from openpyxl.reader.excel import load_workbook, Workbook

from analyze.scope_parse.c_get_lines import get_vol_cur_single
from analyze.scope_parse.d_calc import calc
from analyze.spectrum_parse.c_concentration import ozone_concentration, ozone_ppm

# Folder with measuremtn. Folder has to contain:
# * log.txt
# * spect/m00000.txt  with spectral data
# * scope/000.csv with 000=used input voltage
# run_dir = "G:/Prive/MIJN-Documenten/TU/62-Stage/20171229"
run_dir = "G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run3-800v-width"
spect_dir = '/spect'
scope_dir = '/scope'
log_file = 'log.xlsx'  # must be xlsx with at least [voltage, freq, v18,9ohm input, spectfile, Temp, airflow]
scope_file_name_index = 2  # which column of log.xlsx contains the filename for scope. 0=volt, 1=freq, 2=pulsew

######################
# script starts here #
######################

# Get ozone concentrations:
all_ozone = ozone_concentration(path_name=run_dir+spect_dir)
all_ppm = ozone_ppm(all_ozone)

# assuming format: voltage, freq, voltage on 18,9ohm input, meting spect, Temp, airflow
log_file = run_dir + '/' + log_file
resistor_val = 18.9 # resistance of measure resistor for input current

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
        print("Error! Some empty cells found in: "+str(data_row))
    # 0: voltage        [V]
    # 1: freq           [Hz]
    # 2: duration       [us]
    # 3: v18, 9ohm input[V]
    # 4: spectfile      [filename]
    # 5: Temp           [deg. Cels.]
    # 6: airflow        [ls/min]
    I = data_row[3]/resistor_val  # generator input current [A]
    P = I*data_row[0]  # generator input power [W]
    Pk = P/3.6e6  # input power in kWh/s
    iEp = P/data_row[1]  # input energy per pulse [J]
    #iEpk = iEp / 1000 * 3600  # input energy per pulse {kWh]
    co3 = all_ozone[data_row[4]]  # mol/m3
    co3g = co3 * 48  # gram/m3 o3
    lss = data_row[6]/60  # liter air per second
    m3s = lss/1000  # ls/min/1000/60=m3/s
    o3f = co3g * m3s  # (gram/m3)*(m3/s)=gram/second o3

    # get output waveforms
    try:
        line = get_vol_cur_single(run_dir+scope_dir+'/'+str(data_row[scope_file_name_index])+'.csv')
        output_time, output_v, output_i = line
    except IOError:
        output_time = output_v = output_i = 0
        line = None

    dic = {
        # manually noted values (inputs)
        'input_voltage': data_row[0],   # input voltage in V
        'input_voltage_output': data_row[0]*15,  # excpected output voltage of generator
        'pulse_frequency': data_row[1], # pulse frequency in Hz
        'pulse_duration': data_row[2],  # pulse duration in us.
        'temperature': data_row[5],     # temperature in deg Celsius
        'airflow': data_row[6],         # airflow in ls/min

        # calculated values from noted values. (This is not compensated for resistive losses in generator!!)
        'input_current': I,             # input current to generator
        'input_power': P,               # input power to generator
        'input_pulse_energy': iEp,      # input energy per pulse in Joule
        'input_energy_dens': P / lss,   # input energy to generator in Joule/ Liter used air

        # values from ozone spectrum, as obtained from spectrometer.
        'o3_concentration': co3,        # o3 concentration in Mol/m3
        'o3_ppm': all_ppm[data_row[4]], # o3 concentration in ppm
        'o3_gramsec': o3f,              # o3 production in gram/second

        # scope spectra
        'output_time': output_time,
        'output_voltage': output_v,
        'output_current': output_i,

        # o3 generation efficiency
        'input_yield_gj': o3f/P,          # efficiency in gram/Joule
        'input_yield_gkwh': o3f/Pk,       # efficiency in gram/kWh

    }
    try:
        if line:
            for key,val in calc(line).items():
                dic['output_'+key]=val
    except NameError:
        pass # line does not exist
    data.append(dic)

# save pickle
with open(run_dir+'/data.pkl', 'wb') as f:
    pickle.dump(data, f, )


# save xlsx
wb = Workbook()
ws = wb.active
ws.title = "data"
# make header row. row 5 probably contains all headers, since the first few will miss some as they are reference lines.
keys = []
for key, value in data[4].items():
    # don't save arrays of values, it is too much information
    try:
        value = float(value)
        if not np.isfinite(value):  # replace inf and -inf with 0
            value = 0
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
wb.save(filename = run_dir+'/data.xlsx')

print("finished writing")