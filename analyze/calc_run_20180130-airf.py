from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180130-airf/'
d=-5

# long glass 26uh

calc_run(base + 'run1',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=6,  # airflow
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=80,)

calc_run(base + 'run2',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=6,  # airflow
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=80,)

# different voltage scaling
calc_run(base + 'run2-2',
         REACTOR_GLASS_LONG,
         scope_multiple=True,
         scope_file_name_index=6,  # airflow
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,)