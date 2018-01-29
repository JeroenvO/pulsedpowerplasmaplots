from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180129-airf/'
d=-5
# short quad nocoil
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=6,  # airflow
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30)

# short quad nocoil
calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=6,  # airflow
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=30)