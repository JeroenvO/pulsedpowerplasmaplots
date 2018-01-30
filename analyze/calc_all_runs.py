"""
Execute all calc_run_<date> files in the analyze. directory.
"""
import os
import importlib

# these measurements contains bad ozone data.
blacklist = ['calc_run_20180102.py', 'calc_run_20180103.py', 'calc_run_20180104.py']  # wrong ozone data
blacklist += ['calc_run_20180105.py', 'calc_run_20180110.py', 'calc_run_20180111.py']  # wrong waveforms
gbl = globals()
for toImport in os.listdir('.'):
    if toImport[0:9] == 'calc_run_':
        if toImport not in blacklist:
            moduleToImport = 'analyze.'+toImport[:-3]
            print(moduleToImport)
            gbl[moduleToImport] = importlib.import_module(moduleToImport)