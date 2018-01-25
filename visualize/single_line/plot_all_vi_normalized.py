import matplotlib.pyplot as plt

from visualize.helpers.colors import color_rainbow
from visualize.helpers.data import load_pickle, save_file

data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180103/run2-1us/data.pkl")

# normalize
colors = color_rainbow(len(data))
fig, ax = plt.subplots(2, 1)
fig.suptitle('Normalized waveforms (1us, 1kHz, 26$\mu$H)')
for i, line in enumerate(data):
    c = line['output_current']
    v = line['output_voltage']
    try:
        l = str(line['input_voltage_output'] / 1000) + 'kV'
        c = c / max(c)
        ax[0].plot(line['output_time'], c, label=l, color=colors[i], linewidth=0.5)
        v = v / line['output_v_pulse']
        ax[1].plot(line['output_time'], v, label=l, color=colors[i], linewidth=0.5)
    except:
        pass

ax[0].set_ylabel('normalized current')
ax[1].set_ylabel('normalized voltage')
plt.xlabel('time [s]')
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
ax[0].grid(True)
ax[1].grid(True)
plt.show()
save_file(fig, name='all_vi_normalized', bbox_extra_artists=(lgd,))
# fig.savefig('plot.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
# fig.savefig('plot.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')
print("finish")
