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
from analyze.spectrum_parse.a_spectrasuite_parser import parse_file
from analyze.spectrum_parse.b_trim_spectrum import trim_spectrum
import numpy as np


def ozone_concentration(path_name='G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/spect',
                        opt_path=0.03,
                        plot_spect=False,
                        plot_result=False):
    # read the file
    freqs, vals = parse_file(path_name=path_name, start_index=0)
    # align the spectrum with the molina absorbtion rates, and trim it to an fmin/fmax
    # freqs_meas is as close as possible to freqs_abso. This is validated for default settings of spectrasuite.
    freqs_abso, abso, freqs_meas, vals = trim_spectrum(freqs, vals)

    # convert abso coeff to Mol/m3, it is 10^-20cm^2/molecule
    abso *= 1e-24

    # divide each array of values (= one measurement) by the reference (=vals[0])
    # and calculate ozone concentration in Moles.
    Na = 6.02214e23  # avagadro constant
    results = [-np.log(val / vals[0]) / (opt_path * abso * Na) for val in vals]
    results_mean = [np.mean(result) for result in results]
    if plot_result:
        # validate the stability of the values over frequency.
        import matplotlib.pyplot as plt
        for i, r in enumerate(results):
            plt.plot(freqs_meas, r, label=i)
        #        plt.axhline(results_mean[i])

        plt.legend()
        plt.ylabel('O3 [Mol/m3]')
        plt.xlabel('wavelength [nm]')
        plt.show()
    if plot_spect:
        # check the spectrum
        import matplotlib.pyplot as plt
        markers = [',', '+', '.', 'o', '*', 'v', '>', '<']
        for i, v in enumerate(vals[1:]):
            plt.plot(freqs_meas, v, label=i, linewidth=0.5, marker=markers[i], markersize=1)

        plt.legend(('09:23', '09:40', '09:55', '10:26'))
        plt.title('Since 9:19')
        plt.ylabel('amplitude')
        plt.xlabel('wavelength [nm]')
        plt.savefig('lamp_warming.eps', bbox_inches='tight')
        plt.savefig('lamp_warming.png', bbox_inches='tight')
        plt.savefig('lamp_warming.pdf', bbox_inches='tight')
        plt.show()

    return results_mean


def ozone_ppm(results, temperature=22):
    """
    Calculate ppm for given results array with Mol/m3 concentrion

    :param results: array of results in Mol/m3
    :param temperature: gas measurement temperature in celsius
    :return: array of ppm
    """
    P = 1e5  # pascal
    V = 1  # m3
    R = 8.314472  # JK-1 mol-1
    T = 273 + temperature  # K @ temperature grC

    # Calculate ppm
    n = (P * V) / (R * T)  # total amount of particles in 1000l gas: mol/m3 gas
    ppm = [(result / n) * 1e6 for result in results]

    return ppm
