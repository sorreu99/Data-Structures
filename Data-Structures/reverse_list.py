list = [2, 4, 5, 3]


def reverse_list(list):
    length = len(list)
    for i in range(length - 1):
        temp = list.pop(-1)
        list.insert(i, temp)


reverse_list(list)
print(list)
