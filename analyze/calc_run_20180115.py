from analyze.calc_run import *

# first final measurement for normal pulses.

d=-5 # delay

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180115-def1/'

# short quad nocoil
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30)

# short quad 26uH
calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=None)

# short quad 8uH
calc_run(base + 'run3',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=None)

# short quad nocoil long meas
calc_run(base + 'run4',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=LONG_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30)

# long react 26uH
calc_run(base + 'run5',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=None)

calc_run(base + 'run6',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=None)
