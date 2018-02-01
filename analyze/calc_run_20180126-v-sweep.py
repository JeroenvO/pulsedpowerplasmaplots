from analyze.calc_run import *

# burst mode

d=-5 # delay

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180126-v-sweep/'

# short reactor
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=0,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         waveform_loose_stability=True
         )

calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=0,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=81,
         waveform_loose_stability=True
         )

calc_run(base + 'run3',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=0,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         waveform_loose_stability=True
         )
