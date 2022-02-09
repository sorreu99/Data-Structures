list = [8, 9, 6, 4, 3, 5]
sum = int(input("Enter the sum you want the pair for"))


def sum_pair(sum, list):
    flag = 0
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == sum:
                flag = 1
                print(list[i], list[j])
    if flag == 0:
        return ("No such pair found")


sum_pair(sum, list)
