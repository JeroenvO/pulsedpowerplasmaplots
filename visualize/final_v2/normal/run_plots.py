"""
Run all plot scripts from visualize/final
Used to update all plots for the report at once.
"""
from visualize.final_v2.normal.plot_edens_yield import *
from visualize.final_v2.normal.plot_ppm_yield import *
from visualize.final_v2.normal.plot_edens_yield import *
from visualize.final_v2.normal.plot_pe import *
from visualize.final_v2.normal.plot_vi import *
from visualize.final_v2.normal.plot_f_epulse import *
from visualize.final_v2.normal.plot_v_ppm import *
from visualize.final_v2.normal.plot_l_ppm import *
from visualize.final_v2.normal.plot_f_eff import *
from visualize.final_v2.normal.plot_ppm_yield import *
from analyze.defines import *


datas = load_pickle('20180115-def1/run5')
datas += load_pickle('20180118-def2/run1')
datas += load_pickle('20180119-def3/run1')
datas += load_pickle('20180115-def1/run2')
datas += load_pickle('20180118-def2/run3')
datas += load_pickle('20180118-def2/run3-2')
datas += load_pickle('20180115-def1/run1')
datas += load_pickle('20180118-def2/run2')

for reactor, ind in [(REACTOR_GLASS_LONG, 26), (REACTOR_GLASS_SHORT_QUAD, 0), (REACTOR_GLASS_SHORT_QUAD, 26)]:
    data = filter_data(datas, reactor=reactor, inductance=ind)
    reactor=reactor.replace(' ', '-')
    if ind:
        name = reactor + '-' + str(ind) + 'uH'
    else:
        name = reactor + '-nocoil'

    plot_f_epulse(data, name)
    plot_f_eff(data, name)
# close('all')

plot_edens_yield(datas)
plot_ppm_yield()
# close('all')
#
# plots of a single waveform
for reactor in ['long-glass', 'short-glass']:
    data = []
    if reactor == 'long-glass': # 26uH, long glass,
        data = load_pickle('20180115-def1/run5')
    elif reactor == 'short-glass':
        data = load_pickle('20180115-def1/run1')
    plot_vi_zoom(data, reactor)
    plot_vi(data, reactor)
    plot_pe(data, reactor)
# close('all')

# custom data
for reactor in ['long-glass', 'short-glass']:
    plot_v_ppm([], reactor) # voltage to ppm
    plot_l_ppm([], reactor) # pulsewidth to ppm
# show effect of temperature and pulsewidth
plot_l_ppm([], 'long-glass', voltage=800)

# close('all')