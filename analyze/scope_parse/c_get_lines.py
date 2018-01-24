import os

from analyze.scope_parse.a_easyscope_parser import parse_file
from analyze.scope_parse.b_correct_lines import correct_lines
from analyze.defines import *

def get_vol_cur_single(filename,
                       current_scaling = 0.5,
                       delay=0,
                       voltage_offset=None,
                       current_offset=None):
    """
    Parse voltage and current from waveforms.

    :param filename: filepath without extension
    :return: [time, v, i] of waveform
    """
    line_objs = parse_file(filename)  # file to parse
    offsets = [
        {'v_shift': delay,  # -16 works fine for exact match of waveforms with different cable length. Otherwise 0
        'div_zero': voltage_offset},  # if voltage has another div_zero than current
        {'val_div_correct': current_scaling,  # -100 for Pearson 0.1v/a inverted.
        'div_zero': current_offset}
        # {},
        # {}
    ]

    time_axis, y_axes = correct_lines(line_objs, offsets=offsets)
    v = y_axes[0]
    i = y_axes[1]

    assert MAX_VOLTAGE_MIN < max(v) < MAX_VOLTAGE_MAX, "Voltage max (%r) scaling incorrect!" % max(v)
    assert MIN_VOLTAGE_MIN < min(v) < MIN_VOLTAGE_MAX, "Voltage min (%r) scaling incorrect!" % min(v)

    if not MAX_CURRENT_MIN < max(i) < MAX_CURRENT_MAX:  # max current between 2A and 30A
        if max(i) < 0.03:
            print("Warning!, scope current corrected for mV to V!")
            i *= 1000
        elif max(i) > 1000:  # minimum 1A max
            print("Warning!, scope current corrected for V to mV!")
            i /= 1000
        else:
            raise Exception("Current scaling is incorrect! Max: "+str(max(i))+', Min: '+str(min(i)))
    assert MAX_CURRENT_MIN < max(i) < MAX_CURRENT_MAX, "Current max (%r) scaling incorrect!" % max(i)
    assert MIN_CURRENT_MIN < min(i) < MIN_CURRENT_MAX, "Current min (%r) scaling incorrect!" % min(i)
    # assert i.argmax() < i.argmin(), 'Current valley before peak, signal is inverted!'
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


def get_vol_cur_multiple(base_filename, **kwargs):
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
            # print(base_filename, i)
            lines.append(get_vol_cur_single(base_filename+'_'+str(i),
                         **kwargs))
            i += 1
        except IOError:
            break
        except Exception as e:
            raise Exception(e)
    return lines