import numpy as np

def correct_lines(line_objs, time_point = 1e-9, div_zero = 128.0, div_point = 25, offsets=[]):
    """
    correct and scale scope lines from easyscope parser. Assumes all lines have 0 v_offset (which is point 128)
    Scope is 8-bit, so 256 datapoints. Center is at 128. 25 points/div so little more than 5divs vertical.

    :param file: obj with lines from a_easyscope_parser
    :param time_point: sample size, 1Gs=1ns is default.
    :param div_zero: the vertical zero point. When lines have no offset, this is near 128.
    :param div_point: number of data points per division.
    :param offsets: array of dicts for each data line with [{'v_shift': <int>, 'val_div_correct': <int>}]
    :return: 2d object with x-axis and n y-axes.
    """

    line_length = line_objs[0]['line_length']  # lenght of time axis.
    t_shift = line_objs[0]['t_shift']  # trigger point
    n_lines = len(line_objs)-1

    # make x-axis
    x_axis = np.linspace(-line_length / 2, line_length / 2, line_length) * time_point + t_shift
    # x_div = x_axis[1]-x_axis[0]

    y_axes = []
    for i, line in enumerate(line_objs[1:]): # first line_obj is generic data.
        y = (line['points'] - div_zero) / div_point * line['val_div']  # current
        if offsets:
            if 'val_div_correct' in offsets[i]: # sometimes val_div is not correctly exported. 'mili' tends to be ignored.
                y /= offsets[i]['val_div_correct']
            if 'v_shift' in offsets[i]:  # vertical shift of n-elements to account for delay in probe/cables.
                np.roll(y, offsets[i]['v_shift'])
        y_axes.append(y)

    return [x_axis, y_axes]