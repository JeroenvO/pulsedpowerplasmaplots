import numpy as np

#127.8
def correct_lines(line_objs, div_zero_default=128.0, offsets=[]):
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
    t_div = line_objs[0]['t_div']
    div_point = 25  # vertical
    if t_div == '1.000000u':
        assert line_length == 6000
        sample_rate = 5e8
    elif t_div == '2.500000u':
        assert line_length == 7500
        sample_rate = 2.5e8
    elif t_div == '5.000000u':
        assert line_length == 3000
        sample_rate = 5e7
    else:
        assert float(t_div)  # default, maximum sample rate of 1GSa
        sample_rate = 1e9

    time_point = 1 / sample_rate
    n_lines = len(line_objs) - 1  # usually 2; current and voltage.

    # make x-axis
    x_axis = np.linspace(-line_length / 2, line_length / 2, line_length) * time_point + t_shift
    # x_div = x_axis[1]-x_axis[0]

    y_axes = []
    for i, line in enumerate(line_objs[1:]):  # first line_obj is generic data.
        # each axis in the data

        # set zero point
        div_zero = div_zero_default
        if offsets:
            if 'div_zero' in offsets[i]:
                if offsets[i]['div_zero'] is not None:
                    div_zero = offsets[i]['div_zero']

        assert abs(line['points'][1]-div_zero) < 3, 'Error! Line does not start at zero potential! (zero: %r)' % div_zero
        assert any([(abs(p)-div_zero) > 10 for p in line['points']]), 'Error! Line has low signal!'

        # filter noise around zero.
        y = []
        l = line['points']
        for j, a in enumerate(l):
            if 0 < j < len(l)-1:
                if abs(a-div_zero) <= 1 and abs(l[j-1]-div_zero) <= 1 and abs(l[j+1]-div_zero) <= 1:  # close to zero
                    y.append(div_zero)
                else:
                    # nonzero items
                    y.append(a)
            else:
                # first and last item
                y.append(a)
        y = np.array(y)

        # convert the oscilloscope points to the real waveform
        y = (y - div_zero) / div_point * line['val_div']

        if offsets:
            # sometimes val_div is not correctly exported. 'mili' tends to be ignored.
            # also, the scope cannot set the current probe scaling to 0.5 or 0.1 v/A.
            if 'val_div_correct' in offsets[i]:
                y /= offsets[i]['val_div_correct']
            if 'v_shift' in offsets[i]:  # vertical shift of n-elements to account for delay in probe/cables.
                y = np.roll(y, offsets[i]['v_shift'])


        y_axes.append(y)

    return [x_axis, y_axes]
