# src/diffuser.py
"""
Grover diffusion operator.
"""

def diffuser(qc, key_size=6):
    """
    Grover diffuser acting on the key register only.
    """

    for i in range(key_size):
        qc.h(i)
        qc.x(i)

    qc.h(key_size - 1)
    qc.mcx(list(range(key_size - 1)), key_size - 1)
    qc.h(key_size - 1)

    for i in range(key_size):
        qc.x(i)
        qc.h(i)

