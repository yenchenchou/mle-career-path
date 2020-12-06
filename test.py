def selection_sort(array):
    ls = []
    if not array:
        return -1
    for i in range(len(array)-1):
        min_idx = i
        for j in range(i, len(array)):
            if array[j] > array[min_idx]:
                min_idx = j
        array[i], array[j] = array[j], array[i]
    return array
            