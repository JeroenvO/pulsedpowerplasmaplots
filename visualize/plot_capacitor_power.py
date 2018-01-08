from analyze.scope_parse.c_get_lines import get_vol_cur_single
from analyze.scope_parse.d_calc import calc_output
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.pyplot import plot as pl
from matplotlib.pyplot import show as sh

line = get_vol_cur_single('G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run4-capacitor/scope/500v.csv')
time, v, i = line
c = 237e-12  # pF
i_in = 0.0292063492063492  # A
v_in = 500  # v
v_out = v_in * 15
p_in = i_in * v_in
f = 1000
e_in_pulse = p_in / f
output = calc_output(line)
p_out = v * i
e_cap_expected = 0.5 * c * output['v_pulse'] ** 2
e_cap_output = output['e_rise'][-1]
e_cap_input = e_in_pulse / 2
gen_loss = e_cap_input - e_cap_output  # energy loss per pulse in generator
gen_res = 15 * 15 + 50  # series resistance in generator [Ohm]
res_losses = i ** 2 * gen_res
half = int(len(res_losses) / 2)
res_losses = res_losses[0:half]  # only rising half
res_los = integrate.cumtrapz(res_losses, time[0:half])
e_cap_res = res_los[-1]
# gen_loss_expected =
