import csv

import numpy as np


def parse_file(path_name, base_name='m', padding_digits=5, extension='txt', start_index=0):
    """
    Read all files in a folder and parse them to array of frequencies and values.
    :param path_name: path relative to workdir of the folder with measurements
    :param base_name: name of the files in the folder, the non-changing part
    :param padding_digits: number of digits in the counter in the filename.
    :param extension: extension of the file.
    :param start_index: index number of the first file to use. This file is the reference.
    :return: freqs and values [<array of freqs>, [<array of val>, <array of val>, ..]]
    """
    base_file = path_name + '/' + base_name
    freqs = []  # array of all frequencies
    vals = []  # first array is reference, next arrays are measurements
    file_counter = 0
    row_counter = 0
    while True:
        # make filename from base and incrementing counter, then try to open the file. If it doesn't exists, finish.
        file = base_file + str(file_counter + start_index).zfill(padding_digits) + '.' + extension
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
                    else:  # check frequency consistency
                        if freqs[row_counter] != freq_fl:
                            print("File " + file + " has different frequency axis than reference! Aborting.")
                            break
                    # store values
                    vals[file_counter].append(np.array(float(row[1].replace(',', '.'))))  # values
                    row_counter += 1
        except IOError:
            # File does not exist, all files are finished reading
            break
        except Exception as e:
            print('Something went wrong wile reading the files (' + str(e) + '). Please check: ' + file)
            break
        file_counter += 1
    print('Parsed ' + str(file_counter) + ' files (including reference).')
    assert freqs, "ERROR! No spectra files found. Please check dir: " + path_name
    return [np.array(freqs), vals]
