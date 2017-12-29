#!/bin/python3
from molina_absorbtion import absorbtions
import numpy as np

# min and max values of spectrum
fmin = 245
fmax = 270


def match_molina(freqs):
    """
    Keep only the frequencies of the spectrum that are close to a reference point of molina
    indices of array of the frequencies that are usable.
    
    :param freqs: array with too much frequencies
    :return: freqs filtered list
    """    
    def find_nearest(array,value):
        idx = (np.abs(array-value)).argmin()
        return idx

    # validation of input data. Spectrum should be higher reso than Molina
    # assuming linear frequency axis
    f_diff = freqs[1] - freqs[0]
    r_diff = absorbtions[1][0] - absorbtions[0][0]
    if f_diff > r_diff:
        # high resolution frequency spectrum
        print("The frequency spectrum is of too low resolution. The script is not made for this operation.")
        exit(1)

    # find frequencies in spectrum that we have a reference for
    freq_indices = []  # list of indices of all frequencies of the spectrum that we will use.
    for absorbtion in absorbtions:
        freq_indices.append(find_nearest(freqs, absorbtion[0]))
    return freq_indices


def trim_spectrum(freqs, vals):
    # prune_spectrum to match it up with the molina data
    indices = match_molina(freqs)  # indices of freqs-array that are usable for the script.
    vals = [np.take(val, indices) for val in vals]  # prune vals same as freqs.
    freqs_meas = np.take(freqs, indices)
    freqs_abso, abso = np.array(absorbtions).T  # transpose of molina absorbtions gives absorbtions values array.

    # trim data based on fmin and fmax
    cond = (fmin<=freqs_abso) & (freqs_abso<=fmax)
    freqs_meas = np.extract(cond, freqs_meas)
    freqs_abso = np.extract(cond, freqs_abso)
    abso = np.extract(cond, abso)
    vals = [np.extract(cond, val) for val in vals]

    # convert abso coeff to Mol/m3, it is 10^-20cm^2/molecule
    abso *= 1e-24

    return [freqs_abso, abso, freqs_meas, vals]