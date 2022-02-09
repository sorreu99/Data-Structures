list = [25, 44, 35, 26, 11]

number = int(input("Enter the number to be searched"))


def linear_search(number, list):
    length = len(list)
    for i in range(length):
        if list[i] == number:
            print("number found at index " + str(i))
            return
        if i == length - 1:
            print("Number not found in the list")


def bubble_sort(list):
    length = len(list)
    for i in range(length - 1):
        flag = 0
        for j in range(length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = 1
        if flag == 0:
            return 0


# sorted list [1, 2, 3, 4, 5]
def binary_search(number, list):
    length = len(list)
    l = 0
    r = length - 1

    while True:
        mid = int((l + r) / 2)
        if number == list[mid]:
            key = mid
            break
        if number > list[mid]:
            l = mid + 1
        else:
            r = mid - 1
        if mid == 0 or mid == length - 1:
            print("number not found in the list")
            return
    print("number is found at index ", key)
    print(key)


print("linear search:")
linear_search(number, list)
print("bubble sort:")
bubble_sort(list)
print(list)
print("binary search")
binary_search(number, list)
