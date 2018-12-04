import numpy as np
from input import p, T, g, m


# Значения x на всех слоях(от 0 до T)
# dtype=object сделан для того, чтобы мы могли в x_points записывать
# значения какого угодно типа
x_points = np.empty(T + 1, dtype=object)

# нам удобна структура данных set, так как в ней
# пропускаются дублирующие значения
x_points[0] = set([m])
B_matr = np.zeros([m+T + 1, T + 1])
U_values = np.empty(T, dtype=object)

f_0 = lambda x, u: g(x) + p * u
f = lambda x, u: (x + 1)*(1 - u)


def bellman_fun(x, t, u):
    f0 = f_0(x, u)
    f_x_u = f(x, u)
    B_prev = B_matr[f_x_u][t+1]

    return f0 + B_prev


for t in range(1, T+1):
    current_layer = set()

    for x in x_points[t-1]:
        current_layer.add(x + 1)
        current_layer.add(0)

    x_points[t] = current_layer

last_layer_points = x_points[T]

for x_point in last_layer_points:
    # Нужно найти все значения функций Беллмана на последнем временном слое - T
    # Там они равны соответственно функции g(x)
    B_matr[x_point][T] = g(x_point)

for t in range(T - 1, -1, -1):
    current_x_points = sorted(x_points[t])
    current_points_len = len(current_x_points)
    U_values[t] = np.zeros(current_points_len)

    for i in range(current_points_len):
        x_point = current_x_points[i]
        save_value = bellman_fun(x_point, t, 1)
        out_value = bellman_fun(x_point, t, 0)

        if save_value <= out_value:
            B_matr[x_point][t] = save_value
            U_values[t][i] = 1
        else:
            B_matr[x_point][t] = out_value
            U_values[t][i] = 0

U_vector = np.zeros(T)
U_vector[0] = U_values[0][0]
prev_x = list(x_points[0])[0]


for i in range(1, T):
    prev_U = U_vector[i - 1]
    curr_x = 0
    curr_x_values = list(x_points[i])

    if prev_U is 1:
        curr_x = prev_x + 1

    curr_x_index = curr_x_values.index(curr_x)

    U_vector[i] = U_values[i][curr_x_index]

print(U_vector)
