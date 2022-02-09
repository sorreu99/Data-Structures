arr = [1, 2, 3, 4, 5]


def arr_left_rotation(shift_by, arr):
    temp_arr = []
    for i in range(shift_by):
        temp_var = arr.pop(0)
        print(temp_arr, temp_var)
        temp_arr.append(temp_var)
    for j in range(shift_by):
        arr.append(temp_arr[j])


arr_left_rotation(2, arr)
print(arr)
