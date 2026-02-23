# experiments/plot_6bit.py

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
import matplotlib.pyplot as plt

from src.oracle import oracle
from src.diffuser import diffuser

KEY_SIZE = 6
NUM_ITERATIONS = 6
SHOTS = 1024

qc = QuantumCircuit(2 * KEY_SIZE + 1, KEY_SIZE)

# superposition
for i in range(KEY_SIZE):
    qc.h(i)

# Grover iterations
for _ in range(NUM_ITERATIONS):
    oracle(qc, KEY_SIZE)
    diffuser(qc, KEY_SIZE)

# measure key
for i in range(KEY_SIZE):
    qc.measure(i, i)

backend = AerSimulator()
qc_t = transpile(qc, backend)
result = backend.run(qc_t, shots=SHOTS).result()
counts = result.get_counts()

# reverse bitstrings for readability
counts_readable = {k[::-1]: v for k, v in counts.items()}

# plot
plt.figure(figsize=(8, 4))
plt.bar(counts_readable.keys(), counts_readable.values())
plt.xlabel("Recovered Key")
plt.ylabel("Counts")
plt.title("Grover Key Recovery (6-bit XOR cipher)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("results/hist_6bit.png")
plt.show()
