from analyze.calc_run import *

# burst mode

d=-5 # delay

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180124-burst-1/'

# short reactor
# each run is a pulse, 5 pulses. Changed scope trigger delay. 100hz, 100khz, 5pulse
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=8,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         burst=5)

calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=8,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.5,
         delay=d,
         voltage_offset=30,
         current_offset=125,# misstake in current sclaing :(
         burst=10)

calc_run(base + 'run3',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=8,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         burst=5)

calc_run(base + 'run4',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=8,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         burst=5)