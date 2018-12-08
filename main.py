import numpy as np
from input import equipment_price, T, support_price_g, start_age, bellman_fun, quality, build_x, f



# Значения x на всех слоях(от 0 до T)
# dtype=object сделан для того, чтобы мы могли в x_points записывать
# значения какого угодно типа
x_points = np.empty(T + 1, dtype=object)

# нам удобна структура данных set, так как в ней
# пропускаются дублирующие значения
x_points[0] = set([start_age - 1])
B_matr = np.zeros([start_age+T + 1, T + 1])
U_values = np.empty(T, dtype=object)



for t in range(1, T+1):
    current_layer = set()

    for x in x_points[t-1]:
        current_layer.add(x + 1)
        current_layer.add(0)

    x_points[t] = current_layer

last_layer_points = x_points[T]

for x_point in last_layer_points:
    # Нужно найти все значения функций Беллмана на последнем временном слое - T
    # Там они равны соответственно функции support_price_g(x)
    B_matr[x_point][T] = support_price_g(x_point)

for t in range(T - 1, -1, -1):
    current_x_points = sorted(x_points[t])
    current_points_len = len(current_x_points)
    U_values[t] = np.zeros(current_points_len)

    for i in range(current_points_len):
        x_point = current_x_points[i]
        save_value = bellman_fun(x_point, t, 1, B_matr)
        out_value = bellman_fun(x_point, t, 0, B_matr)

        if save_value < out_value:
            B_matr[x_point][t] = save_value
            U_values[t][i] = 1
        else:
            B_matr[x_point][t] = out_value
            U_values[t][i] = 0

U_solution = np.zeros(T)
U_solution[0] = U_values[0][0]
x_solution = np.zeros(T)
x_solution[0] = start_age - 1
prev_x = list(x_points[0])[0]


for i in range(1, T):
    prev_U = U_solution[i - 1]
    curr_x_values = list(x_points[i])
    curr_x = f(prev_x, prev_U)


    x_solution[i] = curr_x

    curr_x_index = curr_x_values.index(curr_x)

    U_solution[i] = U_values[i][curr_x_index]
    prev_x = curr_x

g_vector = [support_price_g(i) for i in range(T + 1)]
quality = quality(U_solution, equipment_price)
equipment_ages = build_x(U_solution)

print('X = {}'.format(equipment_ages))
print('Support prices - g(x) = {}'.format(g_vector))
print('Quality = {}'.format(quality))
print('Control: U = {}'.format(U_solution))


