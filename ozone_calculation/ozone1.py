#!/bin/python3
"""
Script to determine ozone concentration from spectrometer data.

Using absorbtion coefficients in the Hartley band (200-300nm)
Absortion values taken from: Absolute absorption cross sections of ozone in the 185- to 350-nm wavelength range,
Molina, L. T. Molina, M. J. 1986, http://doi.wiley.com/10.1029/JD091iD13p14501

Assuming smoothed input data. No smoothing is applied to the data

Lambert-Beer law: ln(I(lambda)/I0(lambda)) = C03 * eps(lambda) *d

Jeroen van Oorschot 2017-2018, Eindhoven University of Technology
jeroen@jjvanoorschot.nl
"""
import csv
import numpy
from molina_absorbtion import absorbtions
import numpy as np
# length of the optical path in the measure cell.
opt_path=0.03
#opt_path=0.111

# set the gas temperature
temperature = input('Give the gas temperature [24]')
temperature = int(temperature or 24)

# directory of the files
path_name = input('Please select the directory of files to be calculated ["\\"]') or ''
base_name = input('Give the base name of the files ["m_"]') or 'm_'
padding_digits = input('Give the number of padding digits [5]')
padding_digits = int(padding_digits or 5)
extension = '.txt'
# constants
P = 1e5 # pascal
V = 1 # m3
R = 8.314472 # JK-1 mol-1
T = 273 + temperature # K @ temperature grC

base_file = path_name + '/' + base_name

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

freqs = []  # array of all frequencies
vals = []  # first array is reference, next arrays are measurements
file_counter = 0
row_counter = 0
while True:
    # make filename from base and incrementing counter, then try to open the file. If it doesn't exists, finish.
    file = base_file + str(file_counter).zfill(padding_digits) + extension
    try:
        with open(file, newline='') as f:
            reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            row_counter = 0
            vals.append([])
            for row in reader:
                # replace comma to dot and read as floats
                freq_fl = float(row[0].replace(',', '.'))
                if file_counter == 0:  # reference file, set frequency array
                    freqs.append(freq_fl)
                else: # check frequency consistency
                    if freqs[row_counter] != freq_fl:
                        print("File " + file + " has different frequency axis than reference! Aborting.")
                        break
                # store values
                vals[file_counter].append(float(row[1].replace(',','.')))  # values
                row_counter += 1
    except IOError:
        # File does not exist, all files are finished reading
        break
    except:
        print('something went wrong wile reading the files. Please check: ' + file)
        break
    file_counter += 1
print('Parsed '+str(file_counter)+' files (including reference).')

# assuming linear frequency axis
f_diff = freqs[1] - freqs[0]
r_diff = absorbtions[1][0] - absorbtions[0][0]
if f_diff > r_diff:
    # high resolution frequency spectrum
    print("The frequency spectrum is of too low resolution. The script is not made for this operation.")
    exit(1)

# convert to numpy
freqs = numpy.array(freqs)
#vals = [numpy.array(val) for val in vals]

# find frequencies in spectrum that we have a reference for
f_indices = []  # list of indices of all frequencies of the spectrum that we will use.
r_val = []  # list of absorbtion coefs
f_val = []  # list of measured amplitude
for absorbtion in absorbtions:
    r_freq = absorbtion[0]  # the frequency of Molina
    f_indices.append(find_nearest(freqs, r_freq))
    r_val.append(absorbtion[1])
r_val = np.array(r_val) # convert list to array

vals_filtered = []
for val in vals:
    vals_filtered.append([v for i,v in enumerate(val) if i in f_indices])

# calculate difference for every frequency
# divide each array of values (= one measurement) by the reference
vals_filtered_1 = [-np.log(np.divide(val, vals_filtered[0])) for val in vals_filtered]

print("finished")

Na = 6.02214e23
a = opt_path * r_val * Na
results = []
for val in vals_filtered_1:
    results.append(np.divide(val, a)) #% 0.149

import matplotlib.pyplot as plt
for r in results:
    plt.plot(r)
plt.show()
print('finished')
#ppm = (antwoord / n) * 1e6
