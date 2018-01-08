import os

from analyze.scope_parse.a_easyscope_parser import parse_file
from analyze.scope_parse.b_correct_lines import correct_lines


def get_vol_cur_single(filename):
    """
    Parse voltage and current from waveforms.

    :param filename: filepath without extension
    :return: [time, v, i] of waveform
    """
    line_objs = parse_file(filename + '.csv')  # file to parse
    offsets = [
        {'v_shift': 0},  # -16 works fine for exact match of waveforms
        {'val_div_correct': -100},
        # {},
        # {}
    ]

    time_axis, y_axes = correct_lines(line_objs, offsets=offsets)
    v = y_axes[0]
    i = y_axes[1]
    if not 2 <= max(i) < 30:  # max current between 2A and 30A
        if max(i) < 1:
            i *= 1000
        else:
            raise Exception("Current scaling is incorrect!")
    assert 2 <= max(v) <= 30e3, "Voltage scaling incorrect!"
    return [time_axis, v, i]


def get_vol_cur_dir(path):
    """
    Get list of [[time, vol, cur], .. ] for each file in 'path'

    :param path: search path
    :return: list of lists with time, vol and cur.
    """
    dir = os.listdir(path)
    lines = []
    for file in dir:
        lines.append(get_vol_cur_single(path+'/'+file) + [file])
    return lines


def get_vol_cur_multiple(base_filename):
    """
    Used if multiple scope waveforms are captured per measurement.
    These waveforms are all appended to the data in calc_run.py
    It will be used in e_average.py to calculate average powers for pulses.

    :param base_filename: base filename/path without extension or _.
    :return: list of lists with [time, v, i] waveforms. One for each obtained waveform
    """
    i = 0
    lines = []
    while True:
        try:
            lines.append(get_vol_cur_single(base_filename+'_'+str(i)))
            i += 1
        except:
            break
    return lines