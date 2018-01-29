"""
Jeroen van Oorschot 2017-2018, Eindhoven University of Technology
jeroen@jjvanoorschot.nl
"""

# Measure tubes length, original from matlab -> wrong
# LONG_MEAS_LEN = 0.111
# SHORT_MEAS_LEN = 0.03
# Measure tubes length, as measured on 18-01-2018 by JvO
LONG_MEAS_LEN = 0.113
SHORT_MEAS_LEN = 0.036

# Reactors
# REACTOR_GLASS_LONG = 14E-12  # long glass reactor capacitance
# REACTOR_GLASS_SHORT = 6.2E-12  # short glass reactor capacitance
# REACTOR_GLASS_SHORT_QUAD = 9e-12  # short glass reactor capacitance with four small electrodes parallel
# REACTOR_CERAMIC = 391E-12
# REACTOR_ALIXPRESS = 161E-12

REACTOR_GLASS_LONG = 'long glass'
REACTOR_GLASS_SHORT_QUAD = 'short glass'

# Maxima and minima for waveforms
MIN_CURRENT_MIN = -35
MIN_CURRENT_MAX = -1
MAX_CURRENT_MIN = 0.1
MAX_CURRENT_MAX = 35
MIN_VOLTAGE_MIN = -10e3
MIN_VOLTAGE_MAX = 100 # should be zero, but is higher because of nooi
MAX_VOLTAGE_MAX = 20e3
MAX_VOLTAGE_MIN = 1e3

# valid values for inductor. Change for different inductors
# INDUCTANCE_LONG_REACTOR = [26, 46]
INDUCTANCE_LONG_REACTOR = [26]
INDUCTANCE_SHORT_REACTOR = [0, 26]
# INDUCTANCE_SHORT_REACTOR = [0, 8, 26, 46]

INPUT_RESISTOR = 18.9