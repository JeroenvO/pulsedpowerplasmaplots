import pickle
from visualize.helpers.colors import color_list
import matplotlib.pyplot as plt



file = "G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/data.pkl"
with open(file, 'rb') as f:
    data = pickle.load(f)
# normalize
colors = color_list(len(data))
fig, ax = plt.subplots(2,1)
ax[0].set_title('normalized waveforms for various pulse voltages [kV]')
for i, line in enumerate(data):
    c = line['output_current']
    v = line['output_voltage']
    try:
        c = c/max(c)
        ax[0].plot(line['output_time'], c, label=line['input_voltage_output']/1000, color=colors[i], linewidth=0.5)
        v = v/line['output_v_pulse']
        ax[1].plot(line['output_time'], v, label=line['input_voltage_output']/1000, color=colors[i], linewidth=0.5)
    except:
        pass

ax[0].set_ylabel('normalized current')
ax[1].set_ylabel('normalized voltage')
plt.xlabel('time [s]')
lgd = ax[0].legend(loc='upper left', bbox_to_anchor=(1,1))
plt.show()
fig.savefig('plot.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig('plot.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')
print("finish")