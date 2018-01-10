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
            if count > 1:
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
        range.sort(key=lambda x: x[0])  # sorted by starttime
        return range
    else:
        return range[-1]


def calc_output(line, react_cap, gen_res_high=225, gen_res_low=50):
    """
    Calc all kinds of properties for a line. The line should be an list of arrays.

    :param line: list of arrays: [time, voltage, current]
    :param react_cap: capacitance of used reactor. Used to calculated capacitance loss
    :param gen_res_high: Series resistance of generator on on-switch. Used to calculated resistive loss
    :param gen_res_low: Series resistance of generator on off-switch. Used to calculated resistive loss
    :return: dict with properties of the line.
    """
    # unpack
    t, v, c = line
    t_diff = t[1] - t[0]
    # assert t_diff == 1e-9  # time scale should be 1ns.
    # values based on current measurment. Assuming voltage waveform is aligned.
    cur_peak_time = c.argmax()
    cur_valley_time = c.argmin()
    i_max = max(c)
    assert c[cur_peak_time] == i_max
    i_min = min(c)
    assert c[cur_valley_time] == i_min

    v_min = min(v)
    v_max = max(v)

    # some validation
    assert 500 <= v_max < 30e3, 'Max voltage (' + str(v_max) + 'V) should be between 0.5kV and 30kV!'
    assert 2 <= i_max < 30, 'Max current (' + str(i_max) + 'A) should be between 2A and 30A!'

    # Find the settling time of the current. Than use the time where the current is stable
    # to calculate the final pulse voltage. This pulse final voltage is then used to calculate
    # the settling time and risetime of the voltage.
    i_time_settling_options = [abs(x) < 0.1 * i_max for x in
                               c[0:cur_valley_time]]  # all parts of current inside 10% of maximum, till end of pulse
    ranges = count_ranges(i_time_settling_options)
    range_before, range_pulse = find_longest_ranges(ranges, 2)  # [end, length]
    end_pulse = range_pulse[0]
    i_time_settling = range_pulse[0] - range_pulse[1]
    v_pulse = np.mean(
        v[i_time_settling:end_pulse])  # average of voltage during pulse when current is < 5% of max current
    # all parts of current inside 10% of maximum, till end of pulse
    v_time_settling_options = [abs(x - v_pulse) < (0.1 * v_pulse) for x in v]
    ranges = count_ranges(v_time_settling_options)
    if ranges == []:  # if too much oscillations, a range cannot be found. Increase the bounds:
        # all parts of current inside 10% of maximum, till end of pulse
        v_time_settling_options = [abs(x - v_pulse) < (0.3 * v_pulse) for x in v]
        ranges = count_ranges(v_time_settling_options)
    assert ranges != [], "Error! Line is too unstable."
    pulse = find_longest_ranges(ranges, 1)  # pulse=[end,length]
    settling_end = pulse[0] - pulse[1]
    t_settling_end = t[settling_end]
    v05 = 0.05 * v_pulse
    settling_start = np.where(v > v05)[0][0]
    t_settling_start = t[settling_start]  # when v first rises above 0.05 of final
    t_settling = t_settling_end - t_settling_start
    v10 = 0.1 * v_pulse
    v90 = 0.9 * v_pulse
    t_rise_start = t[np.where(v > v10)[0][0]]
    t_rise_end = t[np.where(v > v90)[0][0]]
    t_rise = t_rise_end - t_rise_start
    rise_rate = (v90 - v10) / (t_rise)
    v_overshoot = v_max / v_pulse
    pulse_stable = int((settling_end + end_pulse) / 2)  # point where the pulse is very stable
    # energy
    p = v * c  # for this to be correct, make sure lines are aligned in b_correct_lines using offset 'v_div'
    e = integrate.cumtrapz(p, t, initial=0)
    p_rise = p[settling_start:pulse_stable]
    e_rise = e[settling_start:pulse_stable][-1]
    p_res = np.append(c[0:pulse_stable] ** 2 * gen_res_high, c[pulse_stable:] ** 2 * gen_res_low)
    # 1/2*C*V^2 is energy stored in capacitor, which is lost after discharging pulse.
    e_cap = 1 / 2 * react_cap * v_pulse ** 2
    e_res = integrate.cumtrapz(p_res, t, initial=0)
    e_plasma = e_rise - e_cap  # energy to plasma is energy in positive pulse except charge on capacitor.

    # Correct the time axis to have 0 at the start of the pulse
    start = t[settling_start]
    t = t - start

    # all these values are added to the pickle and xlsx with 'output_' prepend in calc_run.py
    data = {
        't': t,
        'v': v,
        'c': c,
        'c_min': i_min,
        'c_max': i_max,
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

        'p_res': p_res,
        'e_res': e_res,
        'e_cap': e_cap,
        'e_plasma': e_plasma,

        'start': start,
        'end': t[end_pulse],
        # 'start_index': settling_start,
        # 'end_index': end_pulse,
        # 'test': i_time_settling
    }
    return data
# #
# #test_calc
# from analyze.scope_parse.c_get_lines import get_vol_cur_single
# import matplotlib.pyplot as plt
#
# file = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-100hz/run2-1us/scope/600.csv'
# line = get_vol_cur_single(file)
# vals = calc_output(line)
