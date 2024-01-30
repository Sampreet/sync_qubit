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
_, _, _, _, _, _, sxs, sys, szs = [arr[i][t_mul:] for i in range(len(arr))]
vs = [0 if sxs[i] >= 0.0 else 1 for i in range(len(sxs))]

# plot
plotter = MPLPlotter(
    axes={
        'X' : sxs,
        'Y' : sys,
        'Z' : szs
    }, params={
        'type'              : 'density_unit',
        'palette'           : ['b', 'r'],
        'sizes'             : [0.1, 0.1],
        'styles'            : ['o', 'o'],
        'x_label'           : '$\\langle \\sigma_{x} \\rangle$',
        'x_label_pad'       : -10,
        'x_tick_labels'     : [-1, '', 1],
        'x_tick_pad'        : -2,
        'x_ticks'           : [-1, 0, 1],
        'y_label'           : '$\\langle \\sigma_{y} \\rangle$',
        'y_label_pad'       : -10,
        'y_tick_labels'     : [-1, '', 1],
        'y_tick_pad'        : -2,
        'y_ticks'           : [-1, 0, 1],
        'z_label'           : '$\\langle \\sigma_{z} \\rangle$',
        'z_label_pad'       : -10,
        'z_tick_labels'     : [-1, '', 1],
        'z_tick_pad'        : -2,
        'z_ticks'           : [-1, 0, 1],
        'label_font_size'   : 16,
        'tick_font_size'    : 12,
        'width'             : 3.0,
        'height'            : 3.0,
        'view_aspect'       : [1.0, 1.0, 1.0],
        'view_elevation'    : 16,
        'view_rotation'     : -30,
        'annotations'       : [{
            'text'  : '(c)',
            'xy'    : (0.24, 0.67)
        }]
    }
)
plotter.update(
    vs=vs,
    xs=sxs,
    ys=sys,
    zs=szs
)
plotter.show()