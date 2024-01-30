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
# time span
ts      = np.linspace(0, 25 * t_mul, 25 * t_ssz * t_mul + 1) / Omega
xs      = ts * Omega

# extract values
arr = np.load('data/v3.2_qutip-v4.7.3/qubit_optomech_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz))['arr_0']
_, _, _, _, _, _, sxs, _, _ = [arr[i] for i in range(len(arr))]
sxs_blue = [v if v >= 0.0 else np.nan for v in sxs]
sxs_red = [v if v < 0.0 else np.nan for v in sxs]

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'scatters',
    'colors'            : ['b', 'r'],
    'styles'            : ['o', 'o'],
    'x_label'           : '$\\Omega t / {}$'.format(t_mul),
    'x_tick_labels'     : [i * 5.0 for i in range(6)],
    'x_ticks'           : [i * 5.0 * t_mul for i in range(6)],
    'x_ticks_minor'     : [i * t_mul for i in range(26)],
    'v_label'           : '$\\langle \\sigma_{x} \\rangle$',
    'v_ticks'           : [i * 0.5 - 1.0 for i in range(5)],
    'v_ticks_minor'     : [i * 0.25 - 1.0 for i in range(9)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 4.8,
    'height'            : 2.3,
    'annotations'       : [{
        'text'  : '(a)',
        'xy'    : (0.19, 0.36)
    }]
})
plotter.update(
    vs=[sxs_blue, sxs_red],
    xs=xs
)
plotter.show()