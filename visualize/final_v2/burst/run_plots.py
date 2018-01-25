"""
Run all plot scripts from visualize/final
Used to update all plots for the report at once.
"""
from visualize.final_v2.burst.plot_edens_yield import *
from visualize.final_v2.burst.plot_ppm_yield import *
from visualize.final_v2.burst.plot_f_epulse import *

from visualize.helpers.data import annotate_data
datas = [
    load_pickle('20180124-burst-1/run4'), # 50
    load_pickle('20180125-burst-2/run2'), # 75
    load_pickle('20180124-burst-1/run1'), # 100
    load_pickle('20180124-burst-1/run3'), # 150
    load_pickle('20180125-burst-2/run1'), # 200

    load_pickle('20180124-burst-1/run2'), # 100, 10pulse
    ]

plot_f_epulse(datas)

plot_edens_yield(datas)
