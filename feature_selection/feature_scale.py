def featureScaling(arr):
    max_arr = max(arr)
    min_arr = min(arr)
    ret_list = []

    for i in range(0, len(arr)):
        ret_list.append(float(arr[i] - min_arr) / float(max_arr - min_arr))
    return ret_list