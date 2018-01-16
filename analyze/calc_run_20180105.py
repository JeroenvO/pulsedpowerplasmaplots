from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180105-freq/'
# long reactor normal
calc_run(base + 'run1-1us',
         REACTOR_GLASS_LONG,
         scope_multiple=False,
         scope_file_name_index=1,
         meas=SHORT_MEAS_LEN,
         current_scaling=-0.1,
         delay=0,
         voltage_offset=None)

# run1 short meas
calc_run(base + 'run2-1us-q',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=False,
         scope_file_name_index=1,
         meas=LONG_MEAS_LEN,
         current_scaling=-0.1,
         delay=0,
         voltage_offset=None)
