from allocation.capital import capital_discrete_values, approximate_capital
from allocation.control import control_discrete_values

from math_model.restrictions import is_capital_feasible
from math_model.preconditions import period_time_T
from math_model.capital import next_capital_F
from math_model.target_fn import f_0

from bellman_alg.bellman_fn import boundary_bellman_fn

class BellmanValue:
    def __init__(self, control_v, bellman_value):
        self.u_v = control_v
        self.B = bellman_value

    def get_control(self):
        return self.u_v

    def get_B_value(self):
        return self.B

class BellmanContainer:
    def __init__(self):
        self.boundary_values = [ {
            "capital": capital_v,
            "bellman_value": boundary_bellman_fn(capital_v)
        } for capital_v in capital_discrete_values ]


    def build_last_layer(self):
        for capital_v in capital_discrete_values:
            maximum_value = -float('inf')
            for control_v in control_discrete_values:
                if is_capital_feasible(capital_v, control_v) == False:
                    continue
                
                next_capital_v = approximate_capital(next_capital_F(capital_v, control_v))
                bellman_value = None
                for bellman_v in self.boundary_values:
                    if next_capital_v[0] == bellman_v["capital"][0] and next_capital_v[1] == bellman_v["capital"][0]:
                        bellman_value = bellman_v["bellman_value"]

                res = f_0(capital_v, control_v, period_time_T - 1) + bellman_value

                if res > maximum_value:
                    maximum_value = res
            print(maximum_value)
