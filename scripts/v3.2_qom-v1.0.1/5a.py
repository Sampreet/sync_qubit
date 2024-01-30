# dependencies
import numpy as np

# qom modules 
from qom.ui.plotters import MPLPlotter

# number of trajectories
ntraj   = 1000
# Hilbert space dimension
N       = 30
# normalized optical drive modulation detuning
Omega   = 1.00
# divisions
t_mul   = 500
# step size
t_ssz   = 1
# time span
ts      = np.linspace(0, 25 * t_mul, 25 * t_ssz * t_mul + 1) / Omega
xs      = ts * Omega

# extract values
arr = np.load('data/v3.2_qutip-v4.7.3/qubit_optomech_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz))['arr_0']
_, _, _, _, _, _, sxs, _, _ = [arr[i][:] for i in range(len(arr))]
sxs_blue = [v if v >= 0.0 else np.nan for v in sxs]
sxs_red = [v if v < 0.0 else np.nan for v in sxs]

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'scatters',
    'colors'            : ['b', 'r'],
    'sizes'             : [0.1, 0.1],
    'styles'            : ['o', 'o'],
    'x_label'           : '$\\Omega t / {}$'.format(t_mul),
    'x_label_pad'       : -16,
    'x_tick_labels'     : [0, 25],
    'x_ticks'           : [0, 25 * t_mul],
    'x_ticks_minor'     : [i * 5.0 * t_mul for i in range(6)],
    'v_label'           : '$\\langle \\sigma_{x} \\rangle$',
    'v_label_pad'       : -20,
    'v_tick_labels'     : [0.0, '', 1.0],
    'v_ticks'           : [i * 0.5 for i in range(3)],
    'v_ticks_minor'     : [i * 0.25 for i in range(5)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 2.3,
    'height'            : 2.3,
    'annotations'       : [{
        'text'  : '(a)',
        'xy'    : (0.23, 0.82)
    }]
})
plotter.update(
    vs=[sxs_blue, sxs_red],
    xs=xs
)
plotter.show()