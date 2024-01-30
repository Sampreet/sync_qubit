# dependencies
import numpy as np
import qutip

# limit number of cpus
qutip.settings.num_cpus = 10

# coupling strength
g_q     = 0.04
# normalized time-dependent coefficient lambda
gamma   = 0.02
# number of oscillator states
n_p     = 20
# normalized qubit energy spacing
E_J     = 1.2
# number of trajectories
ntraj   = 1
# Hilbert space dimension
N       = 70
# normalized drive frequency
Omega   = 1.01
# divisor
t_mul   = 100
# step size
t_ssz   = 100
# time span
ts      = np.linspace(0, 25 * t_mul, 25 * t_ssz * t_mul + 1) / Omega

# initial state
psi_0 = qutip.tensor(qutip.basis(N, n_p), (qutip.basis(2, 0) + qutip.basis(2, 1)).unit())
# phonon annihilation operator
b = qutip.tensor(qutip.destroy(N), qutip.qeye(2))
# average phonon number
n_b = b.dag() * b
# position operator
q = (b.dag() + b) / np.sqrt(2)
# momentum operator
p = 1j * (b.dag() - b) / np.sqrt(2)
# sigma X
sx = qutip.tensor(qutip.qeye(N), qutip.sigmax()) 
# sigma Y
sy = qutip.tensor(qutip.qeye(N), qutip.sigmay())
# sigma Z
sz = qutip.tensor(qutip.qeye(N), qutip.sigmaz())

# time-independent Hamiltonian
H_0 = n_b - E_J / 2 * sx + g_q * (b.dag() + b) * sz
# time-dependent coefficient
def H_1_coeff(t, args):
    return gamma * np.sqrt(n_p) * np.cos(Omega * t)
# total Hamiltonian
H = [H_0, [b.dag() + b, H_1_coeff]]
# jump operators
c_ops = [np.sqrt(gamma) * b]

if __name__=='__main__':
    # solve and save
    arr = qutip.mcsolve(H, psi_0, ts, c_ops, [n_b, q, p, sx, sy, sz], ntraj=ntraj, progress_bar=True).expect
    np.savez_compressed('data/v3.2/physrevlett_100_014101_ntraj={}_N={}_Omega={}_t_mul={}_t_ssz={}_irr.npz'.format(ntraj, N, Omega, t_mul, t_ssz), np.array(arr)[:, ::t_ssz])
    