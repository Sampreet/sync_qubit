# dependencies
import numpy as np

# qom modules 
from qom.ui.plotters import MPLPlotter

# coupling strength
g           = 0.04
# normalized time-dependent coefficient lambda
lamb_norm   = 0.02
# number of oscillator states
n_p         = 20
# normalized qubit energy spacing
Omega_norm  = 1.2
# number of trajectories
ntraj       = 1
# Hilbert space dimension
N           = 70
# normalized drive frequency
Omega       = 1.01
# divisor
t_mul       = 1000
# step size
t_ssz       = 100

# extract values
arr = np.load('data/v3.2_qutip-v4.7.3/physrevlett_100_014101_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz))['arr_0']
_, qs, ps, sxs, _, _ = [arr[i][10:] for i in range(len(arr))]
ps_blue = [ps[i] if sxs[i] >= 0.0 else np.nan for i in range(len(sxs))]
ps_red = [ps[i] if sxs[i] < 0.0 else np.nan for i in range(len(sxs))]

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'scatters',
    'colors'            : ['b', 'r'],
    'sizes'             : [0.1, 0.1],
    'styles'            : ['o', 'o'],
    'x_label'           : '$\\langle q \\rangle$',
    'x_label_pad'       : -19,
    'x_tick_labels'     : [-6, '', 6],
    'x_ticks'           : [-6, 0, 6],
    'x_ticks_minor'     : [i * 3 - 6 for i in range(5)],
    'v_label'           : '$\\langle p \\rangle$',
    'v_label_pad'       : -16,
    'v_tick_labels'     : [-6, '', 6],
    'v_ticks'           : [-6, 0, 6],
    'v_ticks_minor'     : [i * 3 - 6 for i in range(5)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 1.9,
    'height'            : 1.9,
    'annotations'       : [{
        'text'  : '(a)',
        'xy'    : (0.28, 0.78)
    }]
})
plotter.update(
    vs=[ps_blue, ps_red],
    xs=qs
)
plotter.show()