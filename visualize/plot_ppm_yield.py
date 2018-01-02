import matplotlib.pyplot as plt
import numpy as np
from visualize.helpers.helpers import load_pickle, get_values
from visualize.helpers.colors import color_list
import matplotlib.pylab as pl

# data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20171229/data.pkl")
data = load_pickle("G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/run1/data.pkl")


y = get_values(data, 'input_yield_gkwh')
x = get_values(data, 'o3_ppm')
v = get_values(data, 'input_voltage_output')
assert len(y) == len(x) == len(v)
colors = color_list(len(x))

fig, ax = plt.subplots()
for ix,iy,ic,iv in zip(x,y,colors,v):
    ax.scatter(ix, iy, c=ic, label=iv)
plt.xlabel('Concentration [PPM]')
plt.ylabel('Yield [g/kWh]')
plt.title('Concentration vs Yield')
lgd = plt.legend((v), loc='upper left', bbox_to_anchor=(1,1))
ax.grid(True)
fig.savefig('plot.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.show()