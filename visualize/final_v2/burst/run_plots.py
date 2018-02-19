"""
Run all plot scripts from visualize/final
Used to update all plots for the report at once.
"""
from visualize.final_v2.burst.plot_burst_ppm import plot_burst_ppm
from visualize.final_v2.burst.plot_edens_yield import *
from visualize.final_v2.burst.plot_f_epulse import *
from visualize.final_v2.burst.plot_ppm_yield import *

plot_f_epulse(load_pickle('20180124-burst-1/run2'))

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

 ]

plot_edens_yield(datas)
plot_ppm_yield(datas)

datas = [load_pickle('20180126-burst-3/run1'),
         load_pickle('20180126-burst-3/run2'),
         ]
# datas += load_pickle('20180130-burst-4/run1')  # burst with 500ns pulses instead of 1us.
plot_burst_ppm(datas)