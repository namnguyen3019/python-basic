def binary_search(nums, target):
    low = 0
    high = len(nums)

    while True:
        mid = (low +high) //2