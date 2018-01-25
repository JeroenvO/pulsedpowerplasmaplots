from analyze.calc_run import *

# ozone spectrum had boxcar width of 8 with these, so measurements less accurate

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-100hz/'

dirs = glob.glob(base + '/run*')
# length of used measure cell
meas_len = SHORT_MEAS_LEN
# capacitance of used reactor
react_cap = REACTOR_GLASS_LONG
# which column of log.xlsx contains the filename for scope. 0=volt, 1=freq, 2=pulsew
scope_file_name_index = 0
# whether multiple scope spectra are stored for each measurement. If true, save as xxx_y.csv with y as index number
scope_multiple = False
# scaling for current sensor is not done in scope, do it manually
current_scaling = -0.1  # 0.5 for red current probe in v-range, -0.1 for pearson (inverted) in v-range, -100 for mv range.
# compensate for delay in line, in array index (=usually 1ns)
delay = 0

for dir in dirs:
    run_dir = dir + '/'
    run_dir = run_dir.replace('\\', '/').replace('//', '/')
    if os.path.isdir(run_dir):
        print(run_dir)
        calc_run(run_dir,
                 meas=meas_len,
                 scope_file_name_index=scope_file_name_index,
                 scope_multiple=scope_multiple,
                 reactor=react_cap,
                 current_scaling=current_scaling,
                 delay=delay)
    else:
        print('Path ' + str(run_dir) + ' does not exist.')


base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180104-500hz/'

dirs = glob.glob(base + '/run*')
# length of used measure cell
meas_len = SHORT_MEAS_LEN
# capacitance of used reactor
react_cap = REACTOR_GLASS_LONG
# which column of log.xlsx contains the filename for scope. 0=volt, 1=freq, 2=pulsew
scope_file_name_index = 0
# whether multiple scope spectra are stored for each measurement. If true, save as xxx_y.csv with y as index number
scope_multiple = False
# scaling for current sensor is not done in scope, do it manually
current_scaling = -0.1  # 0.5 for red current probe in v-range, -0.1 for pearson (inverted) in v-range, -100 for mv range.
# compensate for delay in line, in array index (=usually 1ns)
delay = 0

for dir in dirs:
    run_dir = dir + '/'
    run_dir = run_dir.replace('\\', '/').replace('//', '/')
    if os.path.isdir(run_dir):
        print(run_dir)
        calc_run(run_dir,
                 meas=meas_len,
                 scope_file_name_index=scope_file_name_index,
                 scope_multiple=scope_multiple,
                 reactor=react_cap,
                 current_scaling=current_scaling,
                 delay=delay)
    else:
        print('Path ' + str(run_dir) + ' does not exist.')
