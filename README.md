# Grover-Based Key Recovery on XOR-Based Cryptographic Constructions

This project demonstrates a **Grover-based quantum key recovery attack** on a toy XOR-based cryptographic construction.

A reversible oracle is constructed to mark the correct secret key using **phase kickback**, and **Grover diffusion** is applied to amplify the probability of measuring the correct key.

The project is intended as a **research-oriented educational implementation** illustrating how quantum algorithms can accelerate brute-force attacks on symmetric cryptographic systems.

---

# Project Overview

The attack consists of the following steps:

1. Construct a **reversible XOR oracle**
2. Compare the output with a target value using **all-zero detection**
3. Apply a **phase oracle** via ancilla-based phase kickback
4. Apply the **Grover diffusion operator**
5. Measure the quantum register to recover the secret key

---

# Key Features

* Reversible oracle implementation
* XOR-based toy cipher construction
* Phase oracle using ancilla qubits
* Grover diffusion operator
* Measurement histogram visualization
* Demonstration of **Grover's quadratic speedup**

---

# Project Structure

```
grover-xor-cryptanalysis/

docs/
    oracle_design.md        # Explanation of oracle construction

experiments/
    run_6bit.py             # Fixed 6-bit experiment
    run_nbit.py             # Experiment runner
    plot_6bit.py            # Histogram visualization
    plot_nbit.py            # Plotting utilities

results/
    hist_6bit.png           # Example output histogram

src/
    oracle.py               # Oracle construction
    diffuser.py             # Grover diffusion operator

README.md
```

---

# Requirements

Install the required packages:

```
pip install qiskit qiskit-aer matplotlib numpy
```

Tested with:

* Python 3.10+
* Qiskit
* Qiskit Aer

---

# Running the Experiment

Run the Grover-based key recovery attack using:

```
python3 -m experiments.run_nbit 6 5
```

Where:

| Argument | Description                 |
| -------- | --------------------------- |
| 6        | Key size (6-bit key space)  |
| 5        | Number of Grover iterations |

This performs Grover search over a **6-bit key space**.

---

# Plotting Results

To visualize measurement probabilities:

```
python3 -m experiments.plot_6bit
```

This generates a histogram showing the amplification of the **correct key state** after Grover iterations.

---

# Toy Cipher Definition

The current implementation uses a fixed toy cipher defined by:

```
c = [1, 0, 1, 0, 1, 1]
y_star = [0, 1, 1, 0, 0, 1]
```

Because of this definition, the oracle currently supports **only 6-bit keys**.

---

# Limitations

* The oracle is currently implemented for a **6-bit construction**
* Extending to larger key sizes requires modifying the cipher definition and oracle logic

---

# Future Work

Possible extensions include:

* Generalizing the oracle to **arbitrary n-bit XOR constructions**
* Implementing optimized Grover iteration counts
* Studying larger key spaces
* Integrating noise models from real quantum hardware
* Extending attacks to more complex symmetric primitives

---

# Research Context

Grover's algorithm provides a **quadratic speedup** for brute-force key search.

This project demonstrates how quantum algorithms affect the **security assumptions of symmetric cryptography** and provides a small experimental framework for studying **quantum cryptanalysis**.

---

# License

This project is intended for **educational and research purposes** related to quantum algorithms and cryptanalysis.

