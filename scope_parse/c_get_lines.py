try:
    from b_correct_lines import correct_lines
except ImportError:
    from scope_parse.b_correct_lines import correct_lines
try:
    from a_easyscope_parser import parse_file
except ImportError:
    from scope_parse.a_easyscope_parser import parse_file
    
import os

def get_vol_cur_single(file):
    """
    Parse voltage and current from waveforms.

    :param file:
    :return:
    """
    line_objs = parse_file(file)  # file to parse
    offsets = [
        {'v_shift': -16},
        {'val_div_correct': -100},
        # {},
        # {}
    ]
    time_axis, y_axes = correct_lines(line_objs, offsets=offsets)
    v = y_axes[0]
    i = y_axes[1]

    return [time_axis, v, i]

def get_vol_cur(path):
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
