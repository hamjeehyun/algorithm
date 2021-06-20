arr = [(1, 3), (5, 8), (4, 10), (20, 25)]

def merge(arr):
    sort_list = sorted(arr)
    merge_list = []

    for item in sort_list:
        if merge_list and item[0] < merge_list[-1][1]:
            merge_list[-1] = (merge_list[-1][0], max(item[1], merge_list[-1][1]))
        else:
            merge_list.append(item)

    return merge_list

print(merge(arr))
