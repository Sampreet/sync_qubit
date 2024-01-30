# dependencies
import numpy as np

# qom modules 
from qom.ui.plotters import MPLPlotter

# number of trajectories
ntraj   = 1
# Hilbert space dimension
N       = 75
# normalized optical drive modulation detuning
Omega   = 1.00
# divisions
t_mul   = 500
# step size
t_ssz   = 1

# extract values
arr = np.load('data/v3.2_qutip-v4.7.3/qubit_optomech_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz))['arr_0']
_, _, _, _, qs, ps, sxs, _, _ = [arr[i][t_mul:] for i in range(len(arr))]
ps_blue = [ps[i] if sxs[i] >= 0.0 else np.nan for i in range(len(sxs))]
ps_red = [ps[i] if sxs[i] < 0.0 else np.nan for i in range(len(sxs))]

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'scatters',
    'colors'            : ['b', 'r'],
    'sizes'             : [0.1, 0.1],
    'styles'            : ['o', 'o'],
    'x_label'           : '$\\langle q \\rangle$',
    'x_label_pad'       : -18,
    'x_tick_labels'     : [-8, '', 8],
    'x_ticks'           : [-8, 0, 8],
    'x_ticks_minor'     : [i * 4 - 8 for i in range(5)],
    'v_label'           : '$\\langle p \\rangle$',
    'v_label_pad'       : -18,
    'v_tick_labels'     : [-8, '', 8],
    'v_ticks'           : [-8, 0, 8],
    'v_ticks_minor'     : [i * 4 - 8 for i in range(5)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 1.9,
    'height'            : 1.9,
    'annotations'       : [{
        'text'  : '(d)',
        'xy'    : (0.26, 0.78)
    }]
})
plotter.update(
    vs=[ps_blue, ps_red],
    xs=qs
)
plotter.show()