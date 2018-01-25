from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180111-v-sweep/'

# Multiple waveforms for each measurement are captured, and scope is not averaging.
# Most waveforms have voltage and current of different triggerpoint, this is wrong.

# short quad 100hz
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=0,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.5,
         delay=0,
         voltage_offset=None,
         waveform_loose_stability=True)

# short quad 500hz
calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=0,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.5,
         delay=0,
         voltage_offset=None,
         waveform_loose_stability=True)
