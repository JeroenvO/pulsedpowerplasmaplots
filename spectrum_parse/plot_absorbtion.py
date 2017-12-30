"""
Plot the absorbtion vs wavelength
"""

import matplotlib.pyplot as plt
from molina_absorbtion import absorbtions
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

x = [a[0] for a in absorbtions]
y = [a[1] for a in absorbtions]
plt.xlabel('wavelength ($nm$)')
plt.ylabel('absorbtion ($10^{-20}cm^{2}/molecule$)')
plt.title('absorbtion in Hartley band (ref. Molina)')
plt.plot(x,y)

plt.show()