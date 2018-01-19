from analyze.scope_parse.d_calc import calc_output
import numpy as np


def get_stability(key, loose):
    """
    Required stability in

    :param key: key of the value to get stability for.
    :param loose:
    :return:
    """
    if loose:
        print("Warning! Using loose average stability requirements!")
        if key in ['e_rise', 'v_overshoot', 'e_plasma', 'e_res_total']:
            required_stability = 4
        elif key in ['c_max', 'c_min', 't_rise', 'rise_rate', 't_settling', 'end', 'v_max', ]:
            required_stability = 2
        elif key in ['start']:
            required_stability = 6
        elif key in ['v_min', ]:
            required_stability = 20  # values close to zero have high
        else:
            required_stability = 0.2
    else:
        if key in ['e_rise', 'v_overshoot']:
            required_stability = 0.5
        elif key in ['e_plasma', 'e_res_total']:
            required_stability = 0.2
        elif key in ['c_max', 'c_min', 't_rise', 't_settling', 'end', 'v_max', ]:
            required_stability = 0.8
        elif key in ['rise_rate']:
            required_stability = 4
        elif key in ['v_min']:
            required_stability = 15  # values close to zero have high
        elif key in ['start']:
            required_stability = 100 # start value depends on trigger, which can have changed.
        else:
            required_stability = 0.05
    return required_stability


def calc_output_avg(lines, react_cap, gen_res_high=225, gen_res_low=50, loose_stability=False):
    """
    Average the numeric values of multiple outputs from d_calc.
    List the array values of outputs together.

    :param lines: Lines from c_get_lines. Assumes one measurement has many lines (=scope captures).
    :param react_cap: capacitance of reactor
    :param gen_res_high: resistance on high side, start of pulse
    :param gen_res_low: resistance on low side, end of pulse
    :return: calculated output values, same as d_calc but for multiple inputs.
    """
    output = []
    length = -1
    for i, line in enumerate(lines):
        print('Run calc for line '+str(i))
        if length == -1:
            length = len(line[0])
        else:
            assert len(line[0]) == length
        output.append(calc_output(line, react_cap=react_cap, gen_res_high=gen_res_high, gen_res_low=gen_res_low))

    data = {}
    for key, value in output[-1].items():
        values = [a[key] for a in output]  # all values of this key in output.
        if type(value).__name__ == 'ndarray':
            # add arrays as list of all arrays to final data
            data[key] = values
        else:
            assert np.isfinite(value)
            assert np.isscalar(value)
            data[key] = np.average(values)
            data[key+'_single'] = values
            for i, v in enumerate(values):
                # values should deviate no more than 15% of average, except for some unstable values.
                required_stability = get_stability(key, loose_stability)

                if data[key] != 0 and abs((data[key] - v)/data[key]) > required_stability:
                    raise Exception('Key "' + key + '" with value (' + str(v) + ') in file ' + str(i) +
                                    ' is too far from average (' + str(data[key]) + ') of measurement!')
    # assert len(output[-1]) == len(data)
    return data
