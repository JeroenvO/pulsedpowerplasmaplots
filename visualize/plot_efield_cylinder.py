import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

v_in = 8
a=0.75
a2=2
a3=3
b=7
r=np.arange(a,b,0.125)
E=v_in/(r*np.log(r/a))
E2=v_in/(r*np.log(r/a2))
E3=v_in/(r*np.log(r/a3))

plt.semilogy(r,E, label=str(a))
plt.semilogy(r,E2, label=str(a2))
plt.semilogy(r,E3, label=str(a3))
plt.legend()
plt.title('E field in glass reactor from center to outside.')
plt.xlabel('radius [mm]')
plt.ylabel('E-field (log) [kV/mm]')
plt.grid()
plt.axhline(0.5)
plt.axhline(1.2)
plt.axhline(0.85)
plt.show()