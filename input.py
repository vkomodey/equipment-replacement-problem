import numpy as np
# Стоимость нового оборудования
equipment_price = 10

# Сколько лет проработало оборудование перед к началу планирования
start_age = 2

# На сколько лет необходимо разработать план
T = 18


# Функция, которая показывает стоимость оборудования в зависимости от его возраста
def support_price_g(x):
    return 2*x

# В задаче с p = 10, start_age = 2, T = 4, support_price(x) = 10*x + 10
# ответ = [0 ,1, 0, 1]


def quality(control_vector_u, equipment_price):
    equipment_ages = build_x(control_vector_u)
    quality_result = 0

    for i in range(T):
        new_equipment_price = control_vector_u[i] * equipment_price
        equipment_support_price = support_price_g(equipment_ages[i])

        quality_result = quality_result + new_equipment_price + equipment_support_price

    return quality_result


def f(age, age_decision):
    return (age + 1)*(1 - age_decision)


def f_0(age, age_decision):
    return support_price_g(age) + equipment_price * age_decision


def build_x(control_vector):
    x = np.empty(T + 1)

    x[0] = start_age - 1

    for i in range(T):
        x[i + 1] = f(x[i], control_vector[i])

    return x


def bellman_fun(equipment_age, t, age_decision, Bellman_Values):
    f0 = f_0(equipment_age, age_decision)
    next_age = f(equipment_age, age_decision)

    b_prev = Bellman_Values[next_age][t+1]

    return f0 + b_prev
