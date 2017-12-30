"""
Parse log excel file
Get ozone concentration
Get scope plots

Plot ppm vs g/kWh
etc.

Jeroen van Oorschot 2017-2018, Eindhoven University of Technology
jeroen@jjvanoorschot.nl
"""

from openpyxl.reader.excel import load_workbook
from scope_parse import a_easyscope_parser, b_correct_lines
from spectrum_parse.c_concentration import ozone_concentration, ozone_ppm
import numpy as np
from matplotlib.pyplot import plot,scatter
# Folder with measuremtn. Folder has to contain:
# * log.txt
# * spect/m00000.txt  with spectral data
# * scope/000.csv with 000=used input voltage
run_dir = "G:/Prive/MIJN-Documenten/TU/62-Stage/20171229"

# Get ozone concentrations:
all_ozone = ozone_concentration(path_name=run_dir+'/spect')
all_ppm = ozone_ppm(all_ozone)

# assuming format: voltage, freq, voltage on 18,9ohm input, meting spect, Temp, airflow
log_file = run_dir + '/log.xlsx'
resistor_val = 18.9 # resistance of measure resistor for input current

sheet = load_workbook(filename=log_file, read_only=True).active
data = []
for row in sheet.iter_rows(min_row=2):
    data_row = []
    for cell in row[0:7]:
        # read values from workbook
        data_row.append(cell.value)
    if data_row[0]==None:
        print('finished reading')
        break
    if None in data_row:
        print("Error! Some empty cells found in: "+str(data_row))
           
    # calculate other values
    # 0: voltage (V)
    # 1: frequency (Hz)
    # 2: pulse duration (us)
    # 3: resistor input voltage (V on 18.9Ohm resistor)
    # 4: spectrum measurement
    # 5: temp (degree celsius)
    # 6: airflow (ls/min)
    I = data_row[3]/resistor_val  # generator input current [A]
    P = I*data_row[0]  # generator input power [W]
    Pk = P /1000 * 3600  # input power in kWh/s
    iEp = P/data_row[1]  # input energy per pulse [J]
    iEpk = iEp / 1000 * 3600 # input energy per pulse {kWh]
    co3 = all_ozone[data_row[4]]  # mol/m3
    co3g = co3 * 48 # gram/m3 o3
    ppm = all_ppm[data_row[4]]    # ppm ozone
    lss = data_row[6]/60 # liter air per second
    m3s = lss/1000 # ls/min/1000/60=m3/s
    o3f = co3g/m3s  # (gram/m3)*(m3/s)=gram/second o3
    eff = o3f/P # gram/Joule
    effk = o3f/Pk # gram/kWh
    
    dens = P/lss # J/s / L/s= J/s*s/L = Joule/liter

    data.append(data_row + [I, P, iEp, iEpk, co3, ppm, effk, dens])
    # 7: current input
    # 8: power input
    # 9: input energy per pulse (Joule)
    # 10: input energy per pulse (kWh)
    # 11: o3 concentration mol/m3
    # 12: ppm o3
    # 13: efficiency in gram/Kwh
    # 14: power density in Joule/Liter

p = np.array(data).T

print('finish')