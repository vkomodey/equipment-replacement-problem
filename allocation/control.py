from allocation.utils import allocate
from math_model.restrictions import is_control_feasible

allocated = allocate(0, 1.05, 0.3)
control_discrete_values = list(filter(lambda u: sum(u) <= 1, allocated))
