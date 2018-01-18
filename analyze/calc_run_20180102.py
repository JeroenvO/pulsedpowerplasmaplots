from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180102/'

# ozone spectrum had boxcar width of 8 with these, so measurements less accurate

# long reactor normal
calc_run(base + 'run1',
         REACTOR_GLASS_LONG,
         scope_multiple=False,
         scope_file_name_index=0,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.1,
         delay=0,
         voltage_offset=None)

# run1 short meas
calc_run(base + 'run2-longmeas',
         REACTOR_GLASS_LONG,
         scope_multiple=False,
         scope_file_name_index=0,
         meas=LONG_MEAS_LEN,
         current_scaling=-0.1,
         delay=0,
         voltage_offset=None)

# run1 varying width
calc_run(base + 'run3-800v-width',
         REACTOR_GLASS_LONG,
         scope_multiple=False,
         scope_file_name_index=2,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.1,
         delay=0,
         voltage_offset=None)

# Capacitor
# calc_run(base+'run4-capacitor',
#              REACTOR_GLASS_SHORT_QUAD,
#              scope_multiple = True,
#              scope_file_name_index=1,
#              meas=LONG_MEAS_LEN,
#              current_scaling=0.5,
#              delay=0,
#              voltage_offset=30)
