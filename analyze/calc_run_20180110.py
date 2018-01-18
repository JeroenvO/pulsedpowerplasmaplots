from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180110-lf-sweep/'

# Multiple waveforms for each measurement are captured, and scope is not averaging.
# Most waveforms have voltage and current of different triggerpoint, this is wrong.

# short quad 1 us pulse
calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.5,
         delay=0,
         voltage_offset=None,
         waveform_loose_stability=True) # waveforms are badly triggered.

# short quad 2 us pulse
calc_run(base + 'run3',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.5,
         delay=0,
         voltage_offset=None,
         waveform_loose_stability=True) # waveforms are badly triggered.

# short quad 5 us pulse
calc_run(base + 'run4',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.5,
         delay=0,
         voltage_offset=None,
         waveform_loose_stability=True) # waveforms are badly triggered.

# short quad 26uH 1us pulse
for name in ['', '-2', '-3', '-4']:
    calc_run(base + 'run5'+name,
             REACTOR_GLASS_SHORT_QUAD,
             scope_multiple=True,
             scope_file_name_index=1,
             meas=SHORT_MEAS_LEN,
             current_scaling=-0.5,
             delay=0,
             voltage_offset=None,
             waveform_loose_stability=True) # waveforms are badly triggered.