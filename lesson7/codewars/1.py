def count_positives_sum_negatives(arr):
    if arr == [] : return []
    new_arr = [0, 0]
    for value in arr:
        if value > 0:
            new_arr[0] += 1
        else:
            new_arr[1] += value
    
    return new_arr