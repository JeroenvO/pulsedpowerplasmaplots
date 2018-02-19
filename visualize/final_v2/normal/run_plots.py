"""
Run all plot scripts from visualize/final
Used to update all plots for the report at once.
"""
from analyze.defines import *
from visualize.final_v2.normal.plot_a_ppm import *
from visualize.final_v2.normal.plot_edens_yield import *
from visualize.final_v2.normal.plot_f_eff import *
from visualize.final_v2.normal.plot_f_epulse import *
from visualize.final_v2.normal.plot_l_ppm import *
from visualize.final_v2.normal.plot_pe import *
from visualize.final_v2.normal.plot_ppm_yield import *
from visualize.final_v2.normal.plot_v_ppm import *
from visualize.final_v2.normal.plot_vi import *
from visualize.final_v2.normal.plot_inv_ppm import *

#
# # frequency data
# datas = load_pickle('20180115-def1/run5')
# datas += load_pickle('20180118-def2/run1')
# datas += load_pickle('20180119-def3/run1')
# datas += load_pickle('20180115-def1/run2')
# datas += load_pickle('20180118-def2/run3')
# datas += load_pickle('20180118-def2/run3-2')
# datas += load_pickle('20180115-def1/run1')
# datas += load_pickle('20180118-def2/run2')

# for reactor, ind in [(REACTOR_GLASS_LONG, 26), (REACTOR_GLASS_SHORT_QUAD, 0), (REACTOR_GLASS_SHORT_QUAD, 26)]:
#     data = filter_data(datas, reactor=reactor, inductance=ind)
#     if ind:
#         name = reactor + '-' + str(ind) + 'uH'
#     else:
#         name = reactor + '-nocoil'
#     plot_f_epulse(data, name)
#     plot_f_eff(data, name)
#
# # conclusion plots for frequency data
# plot_edens_yield(datas)
# plot_ppm_yield()


# # plots of a single waveform
# for reactor in [REACTOR_GLASS_LONG, REACTOR_GLASS_SHORT_QUAD]:
#     data = []
#     if reactor == 'long-glass': # 26uH, long glass,
#         data = load_pickle('20180115-def1/run5')
#     elif reactor == 'short-glass':
#         data = load_pickle('20180115-def1/run1')
#     plot_vi_zoom(data, reactor)
#     plot_vi(data, reactor)
#     plot_pe(data, reactor)
#
#
# ## plots of dependency on voltage, waveform data is not good enough.
# data = filter_data(load_pickles('20180126-v-sweep'), input_f=400)  # both reactors on 400hz.
# data += filter_data(load_pickles('20180111-v-sweep'), input_f=100)
# data += filter_data(load_pickles('20180130-v-sweep'), input_f=100)  # long reactor 100 and 400 hz
# reactor = REACTOR_GLASS_LONG
# freqs = [100, 400]
# data1 = filter_data(data, reactor=reactor, inductance=26, input_l=1)
# plot_v_ppm(data1, reactor, freqs)
# reactor = REACTOR_GLASS_SHORT_QUAD
# data2 = filter_data(data, reactor=reactor, inductance=0, input_l=1)
# plot_v_ppm(data2, reactor, freqs)
#
# ## plots of dependency on pulselength
# data = load_pickles('20180130-l')
# # data = load_pickles('20180130-l-other')
# # data += load_pickles('20180202-l')  # data for 5-25 us for different
# reactor = REACTOR_GLASS_LONG
# freqs = [100, 400]
# plot_l_ppm(data, reactor, 1000, freqs)
# reactor = REACTOR_GLASS_SHORT_QUAD
# freqs = [1000, 400]
# plot_l_ppm(data, reactor, 1000, freqs)
#
# ## plot dependency on airflow
# reactor = REACTOR_GLASS_LONG
# freqs = [100, 400]
# data = filter_data(load_pickles('20180130-airf'), input_f=400)
# data += filter_data(load_pickle('20180201-airf/run1'), input_f=100)
# plot_a_ppm(data, reactor, freqs)
# reactor = REACTOR_GLASS_SHORT_QUAD
# freqs = [1000, 400]
# data = load_pickles('20180129-airf')
# plot_a_ppm(data, reactor, freqs)

# inverse
datas = load_pickle('20180115-def1/run5')
datas += load_pickle('20180118-def2/run1')
datas += load_pickle('20180119-def3/run1')
datas += load_pickle('20180115-def1/run2')
datas += load_pickle('20180118-def2/run3')
datas += load_pickle('20180118-def2/run3-2')
datas += load_pickle('20180115-def1/run1')
datas += load_pickle('20180118-def2/run2')
data_nor = filter_data(datas, reactor=REACTOR_GLASS_SHORT_QUAD, inductance=0)
data_inv = load_pickle('20180201-inv/run1')
plot_inv_ppm(data_nor, data_inv)
