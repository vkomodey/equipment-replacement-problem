import numpy as np
from allocation.utils import allocate

start = 100
end = 1100
step = 100

capital_discrete_values = allocate(start, end, step)
seq = list(np.arange(start, end, step))

def approximate_capital(capital_v):
    capital_1 = capital_v[0]
    capital_0 = capital_v[0]

    capital_1_rounded = round(capital_0/step) * step
    capital_2_rounded = round(capital_1/step) * step

    result_capital = np.array([capital_1_rounded, capital_2_rounded])

    if capital_1_rounded > seq[-1]:
        result_capital[0] = seq[-1]
    if capital_1_rounded < seq[0]:
        result_capital[0] = seq[0]

    if capital_2_rounded > seq[-1]:
        result_capital[1] = seq[-1]
    if capital_2_rounded < seq[0]:
        result_capital[1] = seq[0]

    return result_capital

def find_index(capital_v):
    index = -1

    for i, c in enumerate(capital_discrete_values):
        if c[0] == capital_v[0] and c[1] == capital_v[1]:
            index = i
            break

    if index == -1:
        raise Exception("Can't find the index for capital: {}".format(capital_v))

    return index
