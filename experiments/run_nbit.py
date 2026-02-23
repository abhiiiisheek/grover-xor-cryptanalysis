# experiments/run_nbit.py

import sys
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

from src.oracle import oracle
from src.diffuser import diffuser

def run_experiment(KEY_SIZE, NUM_ITERATIONS, SHOTS=1024):
    qc = QuantumCircuit(2 * KEY_SIZE + 1, KEY_SIZE)

    # Initialize uniform superposition
    for i in range(KEY_SIZE):
        qc.h(i)

    # Grover iterations
    for _ in range(NUM_ITERATIONS):
        oracle(qc, KEY_SIZE)
        diffuser(qc, KEY_SIZE)

    # Measure key register
    for i in range(KEY_SIZE):
        qc.measure(i, i)

    backend = AerSimulator()
    qc_t = transpile(qc, backend)
    result = backend.run(qc_t, shots=SHOTS).result()
    counts = result.get_counts()

    # Reverse bitstrings for readability
    return {k[::-1]: v for k, v in counts.items()}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_nbit.py <key_size> <iterations>")
        sys.exit(1)

    key_size = int(sys.argv[1])
    iterations = int(sys.argv[2])

    counts = run_experiment(key_size, iterations)

    for k, v in counts.items():
        print(k, v)
