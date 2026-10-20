import numpy as np 
ket_0=np.array([1,0],dtype=complex)
ket_1=np.array([0,1],dtype=complex)
alpha=3/5
beta=4/5
psi=alpha*ket_0+beta*ket_1
print("quantum state is",alpha*ket_0+beta*ket_1)
norm = np.sum(np.abs(psi)**2)
print(f"\nNormalization check (|α|² + |β|²) = {norm:.6f}")

# Probabilities
prob_0 = np.abs(psi[0])**2
prob_1 = np.abs(psi[1])**2
print(f"P(0) = {prob_0}")
print(f"P(1) = {prob_1}")