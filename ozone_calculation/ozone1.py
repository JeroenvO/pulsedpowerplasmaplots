#!/bin/python3
"""
Script to determine ozone concentration from spectrometer data.

Using absorbtion coefficients in the Hartley band (200-300nm)
Absortion values taken from: Absolute absorption cross sections of ozone in the 185- to 350-nm wavelength range,
Molina, L. T. Molina, M. J. 1986, http://doi.wiley.com/10.1029/JD091iD13p14501

Assuming smoothed input data. No smoothing is applied to the data

Lambert-Beer law: ln(I(lambda)/I0(lambda)) = C03 * eps(lambda) *d

# freqs: frequency - axis
# abso: absorbtion rate for each frequency
# vals: list of spectra for each measurent (=each file). One spectrum = array of values.

Jeroen van Oorschot 2017-2018, Eindhoven University of Technology
jeroen@jjvanoorschot.nl
"""
from a_spectrasuite_parser import parse_file
from b_trim_spectrum import trim_spectrum
import numpy as np

# length of the optical path in the measure cell.
opt_path=0.03
#opt_path=0.111
plot = False
# set the gas temperature
#temperature = input('Give the gas temperature [24]')
#temperature = int(temperature or 24)
temperature = 24
# directory of the files
path_name = input('Please select the directory of files to be calculated ["\\"]') or ''
# base_name = input('Give the base name of the files ["m_"]')
# padding_digits = input('Give the number of padding digits [5]')
# extension = '.txt'
# constants
airflow = input('Please give airflow in ls/min [2ls/min]')
airflow = int(airflow or 2)

Na = 6.02214e23

# read the file
freqs, vals = parse_file(path_name=path_name, base_name='r', start_index=0)
# align the spectrum with the molina absorbtion rates, and trim it to an fmin/fmax
# freqs_meas is as close as possible to freqs_abso. This is validated for default settings of spectrasuite.
freqs_abso, abso, freqs_meas, vals = trim_spectrum(freqs, vals)
# divide each array of values (= one measurement) by the reference (=vals[0])
# and calculate ozone concentration
results = [-np.log(np.divide(val, vals[0]))/(opt_path * abso * Na) for val in vals]
results_mean = [np.mean(result) for result in results]
if plot:
    # validate the stability of the values over frequency.
    import matplotlib.pyplot as plt
    for i,r in enumerate(results):
        plt.plot(freqs_meas, r, label=i)
        plt.axhline(results_mean[i])
    
    plt.legend()
    plt.ylabel('O3 [molecules/m3]')
    plt.xlabel('wavelength [nm]')
    plt.show()

P = 1e5 # pascal
V = 1 # m3
R = 8.314472 # JK-1 mol-1
T = 273 + temperature # K @ temperature grC

# Calculate ppm
n=(P*V)/(R*T)      # total amount of particles in 1000l gas: mol/m3 gas
ppm = [(result / n) * 1e6 for result in results_mean]
print('ppm')
print(ppm)