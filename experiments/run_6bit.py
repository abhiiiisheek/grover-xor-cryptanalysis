# experiments/run_6bit.py

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

from src.oracle import oracle
from src.diffuser import diffuser

KEY_SIZE = 6
NUM_ITERATIONS = 6
SHOTS = 1024

# Total qubits: key + work + flag
qc = QuantumCircuit(2 * KEY_SIZE + 1, KEY_SIZE)

# --- Initialize uniform superposition ---
for i in range(KEY_SIZE):
    qc.h(i)

# --- Grover iterations ---
for _ in range(NUM_ITERATIONS):
    oracle(qc, KEY_SIZE)
    diffuser(qc, KEY_SIZE)

# --- Measure key register ---
for i in range(KEY_SIZE):
    qc.measure(i, i)

# --- Run simulation ---
backend = AerSimulator()
qc_t = transpile(qc, backend)
result = backend.run(qc_t, shots=SHOTS).result()

counts = result.get_counts()

# Print results (correct for little-endian)
for bitstring, count in counts.items():
    print(bitstring[::-1], count)

