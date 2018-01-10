from analyze.scope_parse.d_calc import calc_output
import numpy as np


def calc_output_avg(lines, react_cap, gen_res_high=225, gen_res_low=50):
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
    for line in lines:
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
            for i, v in enumerate(values):
                # values should deviate no more than 10% of average.
                assert abs((data[key] - v)/v) < 0.1,\
                    'Value (' + str(v) + ') in file ' + str(i) + ' is too far from average of measuremnt!'
    assert len(output[-1]) == len(data)
    return data
