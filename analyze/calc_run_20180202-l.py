from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180202-l/'
d=-5

# calc_run(base + 'run1b',
#          REACTOR_GLASS_SHORT_QUAD,
#          scope_multiple=True,
#          scope_file_name_index=2,  # lengt
#          meas=SHORT_MEAS_LEN,
#          current_scaling=0.5,
#          delay=d,
#          voltage_offset=30,
#          )
#
# calc_run(base + 'run2b',
#          REACTOR_GLASS_SHORT_QUAD,
#          scope_multiple=True,
#          scope_file_name_index=2,  # length
#          meas=SHORT_MEAS_LEN,
#          current_scaling=0.5,
#          delay=d,
#          voltage_offset=30,
#          )


calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=2,  # lengt
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         splitted_pulse=True,
         )

calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=2,  # length
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30,
         splitted_pulse=True,
         )

