"""
Calculate all kinds of properties from the scope lines of c_get_lines.py
Assuming lines are aligned (delay is compensated), for instance using b_correct_lines.py

Using definitions of https://nl.mathworks.com/help/control/ref/stepinfo.html
"""
import numpy as np
from scipy import integrate


def count_ranges(a):
    """
    Assumes binary array of 1 and 0 as input. Calculate longest ranges of 1's.

    :param a: array with binary values
    :return: [end_pos, length] of ranges in array
    """
    ranges = []
    count = 0
    for i, v in enumerate(a):
        if v == 1:  # same as previous value
            count += 1
        else:
            if count>1:
                ranges.append([i, count])  # [end, length]
            count = 0
    return ranges


def find_longest_ranges(range, howmany):
    """
    from range of count_ranges, return the 'howmany' longest ranges

    :param range: list of ranges [end, length]
    :param howmany: int, number of ranges to return
    :return: list of 'howmany' [end, length] items, sorted
    """
    range.sort(key=lambda x: x[1])  # sort by length
    if howmany > 1:
        range = range[-howmany:]  # get last few
        range.sort(key=lambda x: x[0]) # sorted by starttime
        return range
    else:
        return range[-1]

def calc(line):
    """
    Calc all kinds of properties for a line. The line should be an list of arrays.

    :param line: list of arrays: [time, voltage, current]
    :return: dict with properties of the line.
    """
    # unpack
    t, v, c = line
    t_diff = t[1]-t[0]
    # assert t_diff == 1e-9  # time scale should be 1ns.
    # values based on current measurment. Assuming voltage waveform is aligned.
    cur_peak_time = c.argmax()
    cur_valley_time = c.argmin()
    i_max = max(c)
    assert c[cur_peak_time ] == i_max
    i_min = min(c)
    assert c[cur_valley_time] == i_min

    v_min = min(v)
    v_max = max(v)
    # Find the settling time of the current. Than use the time where the current is stable
    # to calculate the final pulse voltage. This pulse final voltage is then used to calculate
    # the settling time and risetime of the voltage.
    i_time_settling_options = [abs(x)<0.05*i_max for x in c[0:cur_valley_time]]  # all parts of current inside 10% of maximum, till end of pulse
    ranges = count_ranges(i_time_settling_options)
    range_before, range_pulse = find_longest_ranges(ranges, 2)  # [end, length]
    end_pulse = range_pulse[0]
    i_time_settling = range_pulse[0]-range_pulse[1]
    v_pulse = np.mean(v[i_time_settling:end_pulse])  # average of voltage during pulse when current is < 5% of max current
    v_time_settling_options = [abs(x-v_pulse) < (0.1 * v_pulse) for x in v]  # all parts of current inside 10% of maximum, till end of pulse
    ranges = count_ranges(v_time_settling_options)
    pulse = find_longest_ranges(ranges, 1)  # pulse=[end,length]
    settling_end = pulse[0]-pulse[1]
    t_settling_end = t[settling_end]
    v05 = 0.05*v_pulse
    settling_start = np.where(v > v05)[0][0]
    t_settling_start = t[settling_start] # when v first rises above 0.05 of final
    t_settling = t_settling_end - t_settling_start
    v10 = 0.1*v_pulse
    v90 = 0.9*v_pulse
    t_rise_start = t[np.where(v>v10)[0][0]]
    t_rise_end = t[np.where(v>v90)[0][0]]
    t_rise = t_rise_end - t_rise_start
    rise_rate = (v90-v10)/(t_rise)
    v_overshoot = v_max/v_pulse
    pulse_stable = int((settling_end + end_pulse) /2)# point where the pulse is very stable
    # energy
    p = v*c
    e = integrate.cumtrapz(p, t, initial=0)
    p_rise = p[settling_start:pulse_stable]
    e_rise = e[settling_start:pulse_stable]
    data = {
        'i_min': i_min,
        'i_max': i_max,
        'v_min': v_min,
        'v_max': v_max,
        'v_pulse': v_pulse,
        't_settling': t_settling,
        't_rise': t_rise,
        'rise_rate': rise_rate,
        'v_overshoot': v_overshoot,
        'p': p,
        'e': e,
        'p_rise': p_rise,
        'e_rise': e_rise,
        'test': i_time_settling
    }
    return data
#
# #test_calc
# from scope_parse.c_get_lines import get_vol_cur_single
# import matplotlib.pyplot as plt
#
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/scope/250.csv'
# line = get_vol_cur_single(file)
# vals = calc(line)