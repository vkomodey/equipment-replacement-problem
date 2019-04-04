from bellman_alg.container import BellmanContainer
from math_model.preconditions import startup_kapital_v
from allocation.capital import find_index
from math_model.capital import next_capital_F

bellman_container = BellmanContainer()

bellman_container.build_layers()

grid = bellman_container.get_grid()

capitals = [startup_capital_v]
capital_index = find_index(startup_capital_v)
control = bellman_container.find_control(0, startup_capital_v)
controls = [control]

capitals.append(next_capital_F(capitals[0], controls[0], 0))

for i in range(1, len(grid) - 1):
    controls[i] = bellman_container.find_control(i, capitals[i])
    capitals[i + 1] = next_capital_F(capitals[i], controls[i], i)


print("Controls - {}".format(controls))
print("Capitals - {}".format(capitals))
