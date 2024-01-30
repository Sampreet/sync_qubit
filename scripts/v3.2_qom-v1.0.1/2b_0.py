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
xs      = ts[:20 * t_mul] * Omega

# extract values
arr = np.load('data/v3.2_qutip-v4.7.3/qubit_optomech_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz))['arr_0']
_, _, _, _, qs, _, sxs, _, _ = [arr[i][:20 * t_mul] for i in range(len(arr))]
qs_blue = [qs[i] if sxs[i] >= 0.0 else np.nan for i in range(len(sxs))]
qs_red = [qs[i] if sxs[i] < 0.0 else np.nan for i in range(len(sxs))]

# plot
plotter = MPLPlotter(axes={}, params={
    'type'              : 'lines',
    'colors'            : ['b', 'r'],
    'x_label'           : '$\\Omega t / {}$'.format(t_mul),
    'x_tick_labels'     : [i * 5.0 for i in range(6)],
    'x_ticks'           : [i * 5.0 * t_mul for i in range(6)],
    'x_ticks_minor'     : [i * t_mul for i in range(26)],
    'v_label'           : '$\\langle q \\rangle$',
    'v_label_pad'       : 8,
    'v_ticks'           : [i * 5 - 10 for i in range(5)],
    'v_ticks_minor'     : [i * 2.5 - 10 for i in range(9)],
    'label_font_size'   : 16,
    'tick_font_size'    : 12,
    'width'             : 4.8,
    'height'            : 2.3,
    'annotations'       : [{
        'text'  : '(b)',
        'xy'    : (0.19, 0.36)
    }]
})
plotter.update(
    vs=[qs_blue, qs_red],
    xs=xs
)
plotter.show()