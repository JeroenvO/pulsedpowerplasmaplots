"""
Plot the absorbtion vs wavelength
"""

import matplotlib.pyplot as plt
from analyze.spectrum_parse.molina_absorbtion import absorbtions

x = [a[0] for a in absorbtions]
y = [a[1] for a in absorbtions]
plt.xlabel('wavelength ($nm$)')
plt.ylabel('absorbtion ($10^{-20}cm^2/molecule$)')
plt.title('absorbtion in Hartley band (ref. Molina)')
plt.plot(x,y)
plt.show()