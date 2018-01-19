from analyze.calc_run import *

# second final measurement for normal pulses. Validation and extra check for 20180115

d=-5 # delay

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180119-def3/'

# long reactor 26uH
calc_run(base + 'run1',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=79)