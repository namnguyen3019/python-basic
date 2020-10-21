#       0  1  2  3  4  5  6    7   8   9  10  11  12
list = [1, 2, 3, 4, 5, 7, 10, 26, 29, 45, 50, 60, 70]

def search(number, list):
    found_at = None
    for i in list:
        if i == number:
            found_at = list.index(i)
            break
    return found_at
print(search(1, [2, 2, 3]))

def naive_search(number, list):
    found_at = None
    for i in range(len(list)):
        if list[i] == number:
            found_at = i
            return found_at
    return found_at
print(search(10, list))

def binary_search(number, list):
    found_at = None
    low_number = 0
    high_number = len(list) - 1
    middle_number = (low_number + high_number) // 2

    if list[low_number] == number:
        found_at = low_number
        return found_at
    if list[high_number] == number:
        found_at = high_number
        return found_at
    while low_number+1 != high_number:
        if list[middle_number] == number:
            found_at = middle_number
            return found_at
        elif list[middle_number] > number:
            high_number = middle_number
            middle_number = (high_number + low_number) // 2
        else:
            low_number = middle_number
            middle_number = (high_number + low_number) // 2
    return found_at

print(binary_search(1, list))
