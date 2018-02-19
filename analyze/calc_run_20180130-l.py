from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180130-l/'
d=-5
# short quad nocoil

calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=2,  # lengt
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         scope_dir=None,
         )  # disable waveform parse

calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=2,  # length
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         scope_dir=None,
         ) # disable waveform parse

calc_run(base + 'run3',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=2,  # lengt
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=80,
         scope_dir=None,
         )  # disable waveform parse

calc_run(base + 'run4',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=2,  # length
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=80,
         scope_dir=None,
         ) # disable waveform parse

calc_run(base + 'run1a',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=2,  # lengt
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         )

calc_run(base + 'run2a',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=2,  # length
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         )

calc_run(base + 'run3a',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=2,  # lengt
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=80,
         )

calc_run(base + 'run4a',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=2,  # length
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=80,
         )