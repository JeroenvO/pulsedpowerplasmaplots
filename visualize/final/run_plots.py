"""
Run all plot scripts from visualize/final
Used to update all plots for the report at once.
"""
from visualize.final.plot_edens_yield import *
from visualize.final.plot_pe import *
from visualize.final.plot_vi import *
from visualize.final.plot_f_epulse import *
from visualize.final.plot_v_ppm import *
from visualize.final.plot_l_ppm import *
from matplotlib.pyplot import close

for reactor in ['long-glass-46uH', 'long-glass-26uH', 'short-glass-nocoil', 'short-glass-26uH', 'short-glass-8uH']:
    if reactor == 'long-glass-46uH':
        data = load_pickle("20180115/run6")
    elif reactor == 'long-glass-26uH':
        data = load_pickle("20180115/run5")
    elif reactor == 'short-glass-26uH':
        data = load_pickle("20180115/run2")
    elif reactor == 'short-glass-8uH':
        data = load_pickle("20180115/run3")
    elif reactor == 'short-glass-nocoil':
        data = load_pickle("20180115/run1")
    else:
        raise Exception("No input!")
    plot_edens_yield(data, reactor)
    plot_f_epulse(data, reactor)

close('all')
for reactor in ['long-glass', 'short-glass']:
    data = []
    if reactor == 'long-glass': # 26uH, long glass,
        data = load_pickle('20180115/run5')
    elif reactor == 'short-glass':
        data = load_pickle('20180115/run1')
    plot_vi_zoom(data, reactor)
    plot_vi(data, reactor)
    plot_pe(data, reactor)
    plot_v_ppm([], reactor)
    plot_l_ppm([], reactor)
plot_l_ppm([], 'long-glass', voltage=800)  # show effect of temperature and pulsewidth
close('all')