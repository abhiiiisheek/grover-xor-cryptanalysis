# Oracle Design for XOR-Based Key Recovery

This document describes the construction of the Grover oracle used for quantum
key recovery on an XOR-based cryptographic toy model. The oracle is fully
reversible, introduces no residual garbage, and marks the correct secret key
via phase kickback.

---

## 1. Problem Setting

Let the secret key be a binary string:

k in {0,1}^n

We consider a toy XOR-based construction with a known constant vector `c`
and a known target output `y*`, such that:

y* = k xor c

The attacker’s goal is to recover the unknown key `k` given `c` and `y*`.

---

## 2. Oracle Objective

In Grover’s algorithm, the oracle implements a unitary transformation:

Uf |k> = (-1)^(f(k)) |k>

where the Boolean function `f(k)` is defined as:

f(k) = 1 if k xor c = y*  
f(k) = 0 otherwise

Thus, the oracle must:
1. Identify the unique key satisfying the condition.
2. Apply a phase flip only to that state.
3. Remain fully reversible.

---

## 3. Register Layout

The oracle uses the following quantum registers:

- **Key register**: `n` qubits storing the candidate key |k>
- **Work register**: `n` qubits used for reversible computation
- **Flag ancilla**: 1 qubit used for phase kickback

Total qubits required: `2n + 1`

---

## 4. Reversible XOR Computation

The oracle first computes the XOR operation reversibly:

|k>|0> -> |k>|k xor c>

This is implemented using:
- CNOT gates for copying key bits
- Pauli-X gates to inject the constant `c`

Because XOR is linear and reversible, this step incurs low quantum cost.

---

## 5. Equality Checking via All-Zero Detection

To test whether `k xor c = y*`, the oracle performs the following steps:

1. XOR the known target `y*` into the work register.
2. The work register becomes:

|0...0> iff k is correct

To detect the all-zero state, the oracle:
- Inverts all work qubits
- Applies a multi-controlled X (MCX) gate onto the flag ancilla
- Restores the work register

This sets the flag qubit to |1> if and only if the candidate key is correct.

---

## 6. Phase Kickback

The actual oracle action is performed via **phase kickback**.

A Z gate is applied to the flag qubit:

Z|1> = -|1>

Because the flag is entangled with the key register at this point, the phase
is transferred to the corresponding key state:

|k> -> -|k>

No measurement is performed.

---

## 7. Uncomputation

All intermediate computations are reversed to restore:
- The work register to |0>
- The flag qubit to |0>

After uncomputation, the only remaining effect of the oracle is a phase flip on
the marked key state.

This ensures:
- No garbage qubits
- Compatibility with Grover diffusion
- Correct amplitude amplification

---

## 8. Properties and Limitations

### Properties
- Fully reversible
- Single marked state
- Scales linearly in XOR operations
- Clean separation between oracle and diffuser

### Limitations
- Multi-controlled gates scale poorly with key size
- XOR-only constructions underestimate the cost of realistic ciphers
- Nonlinear Boolean functions (e.g., AND gates) significantly increase depth

These limitations are discussed further in the analysis section.

---

## 9. Summary

This oracle implements a complete and correct marking function for Grover-based
key recovery on XOR-based constructions. While the cipher model is simplified,
the oracle architecture reflects the standard approach used in quantum
cryptanalysis and highlights the practical challenges of scaling Grover attacks.
