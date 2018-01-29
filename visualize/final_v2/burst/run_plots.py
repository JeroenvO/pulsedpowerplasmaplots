"""
Run all plot scripts from visualize/final
Used to update all plots for the report at once.
"""
from visualize.final_v2.burst.plot_edens_yield import *
from visualize.final_v2.burst.plot_ppm_yield import *
from visualize.final_v2.burst.plot_f_epulse import *
from visualize.final_v2.burst.plot_burst_ppm import plot_burst_ppm

from visualize.helpers.data import annotate_data
datas = [
    # 100hz, 5 pulses
    load_pickle('20180124-burst-1/run4'), # 50
    load_pickle('20180125-burst-2/run2'), # 75
    load_pickle('20180124-burst-1/run1'), # 100
    load_pickle('20180124-burst-1/run3'), # 150
    load_pickle('20180125-burst-2/run1'), # 200
    load_pickle('20180126-burst-3/run3'), # 200 extra
    # 200hz, 5 pulses
    load_pickle('20180126-burst-3/run4'),  # 200
    load_pickle('20180126-burst-3/run5'),  # 150
    load_pickle('20180126-burst-3/run6'),  # 100
    load_pickle('20180126-burst-3/run7'),  # 75
    load_pickle('20180126-burst-3/run8'), # 50

    # 50hz, 5 pulses
    load_pickle('20180126-burst-3/run9'),  # 200
    load_pickle('20180126-burst-3/run10'),  # 150
    load_pickle('20180126-burst-3/run11'),  # 100
    load_pickle('20180126-burst-3/run12'),  # 75
    load_pickle('20180126-burst-3/run13'),  # 50

    # 100hz, 10 pulses
    # load_pickle('20180124-burst-1/run2') # 100, 10pulse
]
plot_f_epulse(datas)

plot_edens_yield(datas)

plot_burst_ppm()