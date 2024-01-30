# dependencies
import numpy as np
import qutip

# limit number of cpus
qutip.settings.num_cpus = 10

# normalized primary laser amplitude
A_lp    = 0.4
# normalized laser detuning
Delta   = 1.0
# normalized reference laser amplitude
A_lr    = 0.08
# normalized optical decay rate
kappa   = 0.3
# normalized optomechanical coupling strength
g_o     = 0.3
# normalized mechanical decay rate
gamma   = 0.015
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

# initial state
psi_0 = qutip.tensor(qutip.basis(N, 0), qutip.basis(N, 0))
# photon annihilation operator
a = qutip.tensor(qutip.destroy(N), qutip.qeye(N))
# intracavity photons
n_a = a.dag() * a
# X quadrature
x = (a.dag() + a) / np.sqrt(2)
# Y quadrature
y = 1j * (a.dag() - a) / np.sqrt(2)
# phonon annihilation operator
b = qutip.tensor(qutip.qeye(N), qutip.destroy(N))
# intracavity phonons
n_b = b.dag() * b
# position operator
q = (b.dag() + b) / np.sqrt(2)
# momentum operator
p = 1j * (b.dag() - b) / np.sqrt(2)

# time-independent Hamiltonian in units of (hbar * omega_m)
H_0 = - Delta * n_a - g_o * a.dag() * a * (b.dag() + b) + n_b + 1j * A_lp * (a.dag() - a)
# time-dependent coefficients
def H_lr_a_dag_coeff(t, args):
    return 1j * A_lr * np.exp(- 1j * Omega * t)
def H_lr_a_coeff(t, args):
    return - 1j * A_lr * np.exp(1j * Omega * t)
# total Hamiltonian
H = [H_0, [a.dag(), H_lr_a_dag_coeff], [a, H_lr_a_coeff]]
# jump operators
c_ops = [np.sqrt(kappa) * a, np.sqrt(gamma) * b]

if __name__=='__main__':
    # solve and save
    arr = qutip.mcsolve(H, psi_0, ts, c_ops, [n_a, x, y, n_b, q, p], ntraj=ntraj).expect
    np.savez_compressed('data/v3.2_qutip-v4.7.3/optomech_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz), np.array(arr)[:, ::t_ssz])