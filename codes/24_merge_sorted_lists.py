def merge_sorted_lists(list1, list2):
    merged = []
    i = 0
    j = 0
    len1 = len(list1)
    len2 = len(list2)
    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len1:
        merged.append(list1[i])
        i += 1
    while j < len2:
        merged.append(list2[j])
        j += 1
    return merged

if __name__ == "__main__":
    first_list = [1, 3, 5]
    second_list = [2, 4]
    print("Merged list:", merge_sorted_lists(first_list, second_list))
