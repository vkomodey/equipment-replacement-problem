import numpy as np

def allocate(start, end, step):
    sequence = np.arange(start, end, step)
    seq_len = len(sequence)

    discrete_values = np.zeros([seq_len, seq_len], dtype=object)

    for i in range(seq_len):
        discrete_values[i] = [np.array([sequence[i], sequence[j]]) for j in range(0, seq_len)]

    discrete_values = discrete_values.flatten()

    return discrete_values
