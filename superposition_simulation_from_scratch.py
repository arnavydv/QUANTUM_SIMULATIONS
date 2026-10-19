import numpy as np
ket0 = np.array([1, 0])
ket1 = np.array([0, 1])
alpha = 1 / np.sqrt(2)
beta  = 1 / np.sqrt(2)
psi = alpha * ket0 + beta * ket1
print("State vector |ψ>:", psi)
norm = np.linalg.norm(psi)
print("Norm:", norm)
prob0 = np.abs(psi[0])**2
prob1 = np.abs(psi[1])**2
print(f"P(0) = {prob0:.3f}")
print(f"P(1) = {prob1:.3f}")