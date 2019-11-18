import random


def elim_zeros(input_list):
    while 0 in input_list:
        input_list.remove(0)
    return input_list


def descend_sort(input_list):
    return input_list.sort(reverse=True)


def length_check(number, input_list):
    if number > input_list.len:
        return True
    else:
        return False


def front_elim(number, input_list):
    for x in range(0, number):
        input_list[x] -= 1
    return input_list


def rand_list():
    value_list = []
    for _ in range(10):
        value_list.append(random.randint(0, 10))
    return value_list


def run_default(value_list):

    print(value_list)

    value_list = elim_zeros(value_list)
    print(value_list)

    if len(value_list) == 0:
        print("Pass!")
        return True

    descend_sort(value_list)
    print(value_list)

    num = value_list.pop(0)
    print(value_list)

    if num > len(value_list):
        print("Failed.")
        return False

    value_list = front_elim(num, value_list)
    print(value_list)

    run_default(value_list)


value_list = rand_list()
run_default(value_list)
