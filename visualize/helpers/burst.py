"""
Calculate burst averages

Assumes each line in one measurement is calculated from one of the burst pulses.

"""
import numpy as np

from visualize.helpers.data import get_values


def calc_burst(data):
    """
    Recalculate values from d_calc for a run with bursts where each measurement is one pulse form the burst

    :param data:
    :return:
    """
    pulse_energy = []
    burst_energy = 0
    burst = len(data)
    freq = data[0]['burst_f']
    print("Burst with "+str(burst) + ' pulses')
    pulse_energy = np.average(get_values(data, key='output_e_plasma'))  # average energy in each burst pulse
    burst_energy = sum(get_values(data, key='output_e_plasma')) # sum energy in one burst of n pulses
    output_p_plasma = freq * burst_energy
    lss = np.average(get_values(data, 'airflow_ls'))
    o3f = np.average(get_values(data, 'o3_gramsec'))
    ppm = np.average(get_values(data, 'o3_ppm'))
    input_p = np.average(get_values(data, 'input_p'))
    dic ={
        'e_plasma_burst': burst_energy,
        'e_plasma_avg': pulse_energy,
        'p_plasma': output_p_plasma,
        'output_energy_dens': output_p_plasma / lss,
        'output_yield_gj': o3f / output_p_plasma if output_p_plasma else 0,
        'output_yield_gkwh': o3f / (output_p_plasma / 3.6e6) if output_p_plasma else 0,
        'e_eff': output_p_plasma / input_p if output_p_plasma else 0,
        'ppm': ppm,
    }
    return dic