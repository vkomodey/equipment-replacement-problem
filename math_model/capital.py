from math_model.preconditions import *

# The capital for the next time moment
def next_capital_F(capital_v, control_v):
    def calc_capital(product_type_index):
        amortization = 1 - amortization_mu_v[product_type_index]
        tax = 1 - tax_ro
        bK0 = b[0] * capital_v[0]
        bK1 = b[1] * capital_v[1]

        return amortization * capital_v[product_type_index] + tax * (bK0 + bK1) * control_v[product_type_index]

    return [calc_capital(0), calc_capital(1)]
