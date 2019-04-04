# All variables has a suffix which is equal to appropriate signs
# in the mathematical model from the task. ${variable_name}_{suffix}_{v}
# _{v} postfix indicates that the variable is an array of values(per each product type)

unit_price_p_v = [20, 18] 
salary_w_v = [10, 11]

discounting_bet_i = 0.05

tax_ro = 0.14

amortization_mu_v = [0.05, 0.01]

startup_kapital_v = [300, 500]

capital_priority_alpha = 0.3

production_cost_q_v = [14, 15]

period_time_T = 6

# Production functions are linear, so it is only required to know coefficients for them
production_lin_coeff_v = [1.2, 1.7]

# Work functions are linear, so it is only required to know coefficients for them
work_lin_coeff_v = [0.8, 0.5]

def get_b(product_type_index):
    unit_price = unit_price_p_v[product_type_index]
    production_cost = production_cost_q_v[product_type_index]
    production_lin_coeff = production_lin_coeff_v[product_type_index]
    salary = salary_w_v[product_type_index]
    work_lin_coeff = work_lin_coeff_v[product_type_index]

    return (unit_price - production_cost) * production_lin_coeff - salary*work_lin_coeff

b = [get_b(0), get_b(1)]
