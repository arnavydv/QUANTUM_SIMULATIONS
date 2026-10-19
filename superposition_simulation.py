from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

circuit= QuantumCircuit(1,1)
circuit.h(0)
circuit.measure(0,0)
print(circuit.draw(output="text"))
simulator = AerSimulator()
compiled = transpile(circuit, simulator)
job = simulator.run(compiled, shots=1024)
counts = job.result().get_counts()
print("Measurement results:", counts)