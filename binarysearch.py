def BinarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        center = int((low + high)/2)
        guess = list[center]
        if guess == item:
            return center
        if guess > item:
            high = center - 1
        else:
            low = center + 1
    return None