list = [8, 4, 9, 2, 76, 34, 54, 1]


# finds the minimum number and puts in the front of unsorted array
def selection_sort(list):
    length = len(list)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]


# compares the number and in each pass the largest number moves to the extreme right
def bubble_sort(list):
    length = len(list)
    for i in range(length - 1):
        flag = 0
        for j in range(length - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = 1
        if flag == 0:
            return 0


def insertion_sort(list):
    length = len(list)
    for i in range(1, length):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp


# insertion_sort(list)
# bubble_sort(list)
selection_sort(list)
print(list)


