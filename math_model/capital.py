from math_model.preconditions import *

# The capital for the next time moment
def capital_fn(product_type_index):
    def calculate_capital(prev_K_v, prev_control_u_v):
        amortization = 1 - amortization_mu_v[product_type_index]
        tax = 1 - tax_ro
        bK0 = b[0] * prev_K_v[0]
        bK1 = b[1] * prev_K_v[1]

        return amortization * prev_K_v[product_type_index] + tax * (bK0 + bK1) * prev_control_u_v[product_type_index]

    return calculate_capital

capital_K_v = [capital_fn(0), capital_fn(1)]
