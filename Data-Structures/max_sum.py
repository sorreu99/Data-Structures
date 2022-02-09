list = [3, 2, 1, 4]


def find_sum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + i * (list[i])
    return sum
count = 0
highest_sum = 0
for i in range(len(list)):
    x = find_sum(list)
    if x > highest_sum:
        highest_sum = x
        arr_rotation = count
    list.append(list.pop(0))
    count += 1

print(highest_sum, "with rotation of ", arr_rotation)

