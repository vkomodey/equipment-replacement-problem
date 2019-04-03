from math_model.preconditions import *

def phi(capital_v):
    return capital_priority_alpha * sum(capital_v) / ( 1 + discounting_bet_i )**period_time_T

def target_function(all_capitals, all_controls):
    capitals = all_capitals[0:-1]
    controls = all_controls[0:-1]

    def generic_member(t, capital_v):
        return (1 - tax_ro) * (b[0]*capital_v[0] + b[1]*capital_v[1]) / (1+discounting_bet_i)**t

    first_sum = sum([ generic_member(t, capitals[t]) * ( 1 - controls[t][0] ) for t in range(0, period_time_T - 1)])
    second_member = sum([ generic_member(t, capitals[t]) * ( 1 - controls[t][1] ) for t in range(0, period_time_T - 1)])

    result = phi(all_capitals[-1]) + first_member + second_member

    return result
