from analyze.calc_run import *

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180130-burst-4/'
d=-5
# short quad nocoil
# run 1 is only spectra, no waveforms.
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         meas=SHORT_MEAS_LEN,
         burst=5,
         scope_dir=None,
        )