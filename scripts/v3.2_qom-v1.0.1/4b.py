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
_, _, _, _, qs, ps, sxs, sys, szs = [arr[i][t_mul:] for i in range(len(arr))]
phis = np.array([np.arctan2(sys[i], szs[i]) for i in range(len(sxs))])
thetas = np.array([np.arctan2(sys[i] / np.sin(phis[i]), sxs[i]) for i in range(len(sxs))])
psis = np.array([np.arctan2(-ps[i], qs[i]) for i in range(len(sxs))])
thetas_blue = [thetas[i] if sxs[i] >= 0.0 else np.nan for i in range(len(sxs))]
thetas_red = [thetas[i] if sxs[i] < 0.0 else np.nan for i in range(len(sxs))]

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'scatters',
    'colors'            : ['b', 'r'],
    'sizes'             : [0.1, 0.1],
    'styles'            : ['o', 'o'],
    'x_label'           : '$\\psi / \\pi$',
    'x_label_pad'       : -16,
    'x_tick_labels'     : [-1.0, '', 1.0],
    'x_ticks'           : [-np.pi, 0.0, np.pi],
    'x_ticks_minor'     : [i * 0.5 * np.pi - np.pi for i in range(5)],
    'v_label'           : '$\\theta / \\pi$',
    'v_label_pad'       : -18,
    'v_tick_labels'     : [0.0, '', 1.0],
    'v_ticks'           : [0.0, np.pi / 2, np.pi],
    'v_ticks_minor'     : [i * 0.25 * np.pi for i in range(5)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 2.3,
    'height'            : 2.3,
    'annotations'       : [{
        'text'  : '(b)',
        'xy'    : (0.24, 0.8)
    }]
})
plotter.update(
    vs=[thetas_blue, thetas_red],
    xs=psis
)
plotter.show()