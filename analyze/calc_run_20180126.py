from analyze.calc_run import *

# burst mode

d=-5 # delay

base = 'G:/Prive/MIJN-Documenten/TU/62-Stage/20180126-burst-3/'

# run 1 and 2 are only spectra, no waveforms.
calc_run(base + 'run1',
         REACTOR_GLASS_SHORT_QUAD,
         meas=SHORT_MEAS_LEN,
         burst=5,
         scope_dir=None,
        )
calc_run(base + 'run2',
         REACTOR_GLASS_SHORT_QUAD,
         meas=SHORT_MEAS_LEN,
         burst=10,
         scope_dir=None,
        )

# short reactor
# each run is a pulse, 5 pulses. Changed scope trigger delay. 100hz, 100khz, 5pulse
for i in range(3, 14):
    calc_run(base + 'run'+str(i),
         REACTOR_GLASS_SHORT_QUAD,
         scope_multiple=True,
         scope_file_name_index=8,
         meas=SHORT_MEAS_LEN,
         current_scaling=0.5,
         delay=d,
         voltage_offset=29,
         burst=5,
         spect_dir='../spect-3-13',
        )