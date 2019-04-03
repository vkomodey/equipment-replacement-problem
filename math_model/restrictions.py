from math_model.preconditions import *

def capital_boundary_fn(product_type_index):
    def boundary(capital_value_v):
        bk0 = b[0] * capital_value_v[0]
        bk1 = b[0] * capital_value_v[1]

        return amortization_mu_v[product_type_index] * capital_value_v[product_type_index] / (1 - tax_ro) / (bk0 + bk1)

    return boundary

capital_boundary = [capital_boundary_fn(0), capital_boundary_fn(1)]

def is_control_feasible(u_v):
    return sum(u_v) <= 1

def is_capital_feasible(capital_value_v, control_value_v):
    def is_feasible(product_type_index):
        return capital_boundary[product_type_index](capital_value_v) <= control_value_v[product_type_index] < 1

    return is_feasible(0) and is_feasible(1)
