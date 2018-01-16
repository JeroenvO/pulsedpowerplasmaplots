import matplotlib.pyplot as plt

from visualize.helpers.helpers import save_file, set_plot, load_pickle, get_values, filter_data

data = []
reactor = 'short-glass'
# reactor = 'long-glass'
if reactor == 'long-glass': # 26uH, long glass,
    data += load_pickle('20180115/run5')
elif reactor == 'short-glass':
    data += load_pickle('20180115/run1')

data = filter_data(data, input_f=10)[0]

x_axis = data['output_t'][0]*1e6
v_axis = data['output_v'][0]/1e3
i_axis = data['output_c'][0]

fig, ax1 = plt.subplots()

ax1.plot(x_axis, i_axis, 'b-')

ax1.set_ylabel('current [A]', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(x_axis, v_axis, 'r-')  # voltage

ax2.set_ylabel('voltage [kV]', color='r')

ax2.tick_params('y', colors='r')

set_plot(fig, pulse=True)
save_file(fig, name='vi-'+reactor, path='G:/Prive/MIJN-Documenten/TU/62-Stage/05_python/plots_final')