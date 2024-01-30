# dependencies
import numpy as np

# qom modules 
from qom.ui.plotters import MPLPlotter

# number of trajectories
ntraj   = 400
# Hilbert space dimension
N       = 30
# normalized optical drive modulation detuning
Omega   = 0.98
# divisions
t_mul   = 100
# step size
t_ssz   = 1
# time span
ts      = np.linspace(0, 25 * t_mul, 25 * t_ssz * t_mul + 1) / Omega
xs      = (ts[2 * t_mul:] * Omega) % (2 * np.pi) - np.pi

# extract values
arr = np.load('data/v3.2_qutip-v4.7.3/optomech_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz))['arr_0']
_, _, _, _, qs, ps = [arr[i][2 * t_mul:] for i in range(len(arr))]
psis = np.array([np.arctan2(-ps[i], qs[i]) for i in range(len(qs))])

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'scatters',
    'colors'            : ['b', 'r'],
    'sizes'             : [0.1, 0.1],
    'styles'            : ['o', 'o'],
    'x_label'           : '$\\Omega t / \\pi$',
    'x_label_pad'       : -16,
    'x_tick_labels'     : [-1.0, '', 1.0],
    'x_ticks'           : [-np.pi, 0.0, np.pi],
    'x_ticks_minor'     : [i * 0.5 * np.pi - np.pi for i in range(5)],
    'v_label'           : '$\\psi / \\pi$',
    'v_label_pad'       : -22,
    'v_tick_labels'     : [-1.0, '', 1.0],
    'v_ticks'           : [-np.pi, 0.0, np.pi],
    'v_ticks_minor'     : [i * 0.5 * np.pi - np.pi for i in range(5)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 2.3,
    'height'            : 2.3,
    'annotations'       : [{
        'text'  : '(d)',
        'xy'    : (0.25, 0.82)
    }]
})
plotter.update(
    vs=psis,
    xs=xs
)
plotter.show()