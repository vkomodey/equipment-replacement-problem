from allocation.control import control_discrete_values
from allocation.capital import capital_discrete_values
from bellman_alg.bellman_fn import boundary_bellman_fn
from bellman_alg.container import BellmanValue, BellmanContainer

bellman_container = BellmanContainer()

bellman_container.build_last_layer()
