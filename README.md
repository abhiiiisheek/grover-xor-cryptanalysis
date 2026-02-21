# Grover-Based Key Recovery on XOR-Based Cryptographic Constructions

This project implements a Grover-based quantum key recovery attack on a toy
XOR-based cryptographic construction. A fully reversible oracle is constructed
to mark the correct secret key via phase kickback, followed by Grover diffusion
to amplify its probability.

## Key Features
- Reversible XOR oracle construction
- Equality checking via all-zero detection
- Phase oracle using ancilla-based kickback
- Successful recovery of 6-bit secret keys

## Structure
- `src/` – Oracle and diffuser implementations
- `experiments/` – Reproducible attack scripts
- `results/` – Output histograms and plots
- `docs/` – Technical explanations and limitations

## Requirements
- Qiskit
- Qiskit Aer

## Running the 6-bit attack
```bash
python experiments/run_6bit.py

