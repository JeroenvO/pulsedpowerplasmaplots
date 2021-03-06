"""
Parse data csv export from LeCroy EasyScope, using an WaveAce224 digital oscilloscope.
"""
import numpy as np
import matplotlib.pyplot as plt

multipliers = {
    'n': 1e-9,
    'u': 1e-6,
    'm': 1e-3,
    'k': 1e3,
    'M': 1e6,
    'G': 1e9,
}


def split_multiplier(string):
    """
    Split a string of "1k" in number and letter.

    :param string: number with character multiplier as string
    :return: number, char
    """
    nr = ''
    tx = ''
    for char in string:
        if char.isdigit() or char == '-' or char == '.':
            nr += char
        else:
            tx += char
    return float(nr), tx.strip()


def to_nr(string):
    """
    Set a string of number and character multiplier to float.

    :param string: input
    :return: float
    """
    nr, tx = split_multiplier(string)
    try:
        return nr * multipliers[tx[0]]
    except:
        return float(nr)


def parse_file(file='ceramic-700v-measure.csv', prepend_length=4, append_length=5):
    """
    Parse easyscope csv file.

    :param file: the file to parse
    :param prepend_length: number of textlines before the dataline starts (datalengt, a, b, c)
    :param append_length: number of textlines after the dataline starts (t_div, t_shift, val_div, d, trigg'd)
    :return: line_obj list. First element is general info dict, further elements are data lines in dict.
    """

    if file[-4:] != '.csv':
        file = file + '.csv'
    with open(file, newline='') as f:
        content = f.readlines()
        line_length = int(content[0])  # length of the datapoint of a line
        data_length = line_length + prepend_length + append_length  # total length of one line including variables
        nr_lines = int(len(content) / (data_length))  # number of lines
        line_objs = [{'t_shift': None, 'line_length': line_length, 't_div': None}]
        lines = [content[data_length * i:data_length * (1 + i)] for i in
                 range(nr_lines)]  # split content into the multiple lines
        for i, line in enumerate(lines):
            print("File "+file+" line "+str(i)+' :', end='')
            vars = line[-append_length:]
            if vars[4] == 'Trig\'d\r\n':
                raise Exception('Scope was not paused, it was triggered! File:' + file)
            elif vars[4] == 'Stop\r\n':
                print('Scope was paused.')
            else:
                raise Exception('Scope was not paused and not triggered! File: ' + file)
            t_div = vars[0].strip()
            t_shift = to_nr(vars[1])
            val_div = to_nr(vars[2])
            line_objs.append({
                'points': np.array([int(i) for i in line[prepend_length:-append_length]], float),
                'val_div': val_div,
                'd': int(vars[3]),
            })
            if line_objs[0]['t_shift'] is None:
                line_objs[0]['t_shift'] = t_shift
            else:
                assert line_objs[0][
                           't_shift'] == t_shift, "Data lines are inconsistent! t_shift is not the same for each line."
            if line_objs[0]['t_div'] is None:
                line_objs[0]['t_div'] = t_div
            else:
                assert line_objs[0][
                           't_div'] == t_div, "Data lines are inconsistent! t_div is not the same for each line."
        return line_objs
