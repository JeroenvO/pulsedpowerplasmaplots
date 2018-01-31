from analyze.calc_run import *

# burst mode

d=-5 # delay

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180131-compare/'

# run 1 and 2 are only spectra, no waveforms.
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         meas=SHORT_MEAS_LEN,
         scope_dir=None,
        )
calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         meas=LONG_MEAS_LEN,
         scope_dir=None,
        )

calc_run(base + 'run1-2',
         REACTOR_GLASS_SHORT_QUAD,
         meas=SHORT_MEAS_LEN,
         scope_dir=None,
        )
calc_run(base + 'run2-2',
         REACTOR_GLASS_SHORT_QUAD,
         meas=LONG_MEAS_LEN,
         scope_dir=None,
        )