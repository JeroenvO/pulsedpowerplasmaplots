import matplotlib.pyplot as plt
import numpy as np
try:
    from scope_parse.c_get_lines import get_vol_cur
except:
    from c_get_lines import get_vol_cur
run_dir = "G:/Prive/MIJN-Documenten/TU/62-Stage/20171229"

import operator, functools
def get_values(key):
    return functools.partial(map, operator.itemgetter(key))

line_objs = get_vol_cur(run_dir+'/scope')  # file to parse

# normalize
cur = []
for line in line_objs:
    c = line[2]
    c = (c/max(c))
    plt.plot(line[0], c, label=line[3])
ax.set_prop_cycle('color',plt.cm.spectral(np.linspace(0,1,30)))
plt.ylabel('normalized current')
plt.xlabel('time [s]')
plt.legend(loc='best')
plt.show()
