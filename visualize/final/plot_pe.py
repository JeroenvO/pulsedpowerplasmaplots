import matplotlib.pyplot as plt

from visualize.helpers.helpers import load_pickle, save_file, filter_data, set_plot
data = []
# reactor = 'long-glass'
reactor = 'short-glass'
if reactor == 'long-glass': # 26uH, long glass,
    data += load_pickle('20180115/run5')
elif reactor == 'short-glass':
    data += load_pickle('20180115/run1')
data = filter_data(data, input_v_output=15e3)
data = filter_data(data, input_f=10)

lw = 0.4  # linewidth
fig, ax = plt.subplots(2, 1, sharex=True)
for i, line in enumerate(data):
    for i in range(len(line['output_t'])):
        p = line['output_p'][i]/1e3
        e_out = line['output_e'][i]*1e3
        t = line['output_t'][i]*1e6
        # p_res = line['output_p_res'][i]/1e3
        # e_res = line['output_e_res'][i]*1e3
        # e_in = line['input_p'] / line['input_f']
        ax[0].plot(t, p)
        ax[1].plot(t, e_out, label='reactor', color='red', linewidth=lw)
ax[0].set_ylabel('P [kW]')
ax[1].set_ylabel('E [mJ]')
set_plot(fig, 2, pulse=True)
save_file(fig, name='pe-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')