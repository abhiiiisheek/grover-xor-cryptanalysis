# src/oracle.py
"""
Grover oracle for XOR-based key recovery.

Marks the correct key by applying a phase flip
using reversible XOR computation and equality checking.
"""

def oracle(qc, key_size=6):
    """
    Grover oracle that flips the phase of the correct key.

    Registers (fixed layout):
    - key qubits:     [0 .. key_size-1]
    - work qubits:    [key_size .. 2*key_size-1]
    - flag ancilla:   [2*key_size]
    """

    # Known constant and target (toy cipher)
    c = [1, 0, 1, 0, 1, 1]
    y_star = [0, 1, 1, 0, 0, 1]

    # --- Compute work = key ⊕ c ---
    for i in range(key_size):
        qc.cx(i, i + key_size)
        if c[i] == 1:
            qc.x(i + key_size)

    # --- Compare with target y* ---
    for i in range(key_size):
        if y_star[i] == 1:
            qc.x(i + key_size)

    # --- All-zero detection ---
    for i in range(key_size):
        qc.x(i + key_size)

    qc.mcx(list(range(key_size, 2 * key_size)), 2 * key_size)

    # --- Phase flip (oracle action) ---
    qc.z(2 * key_size)

    # --- Uncompute ---
    qc.mcx(list(range(key_size, 2 * key_size)), 2 * key_size)

    for i in range(key_size):
        qc.x(i + key_size)

    for i in range(key_size):
        if y_star[i] == 1:
            qc.x(i + key_size)

    for i in range(key_size):
        if c[i] == 1:
            qc.x(i + key_size)
        qc.cx(i, i + key_size)

