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
    list1 = []
    for _ in range(10):
        list1.append(random.randint(0, 10))
    return list1


def run_default(list1):

    print(list1)

    list1 = elim_zeros(list1)
    print(list1)

    if len(list1) == 0:
        print("Pass!")
        return True

    descend_sort(list1)
    print(list1)

    num = list1.pop(0)
    print(list1)

    if num > len(list1):
        print("Failed.")
        return False

    list1 = front_elim(num, list1)
    print(list1)

    run_default(list1)


list1 = rand_list()
run_default(list1)
