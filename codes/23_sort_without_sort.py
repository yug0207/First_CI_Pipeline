def bubble_sort(numbers):
    result = list(numbers)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

if __name__ == "__main__":
    sample_list = [5, 2, 9, 1]
    print("Sorted list:", bubble_sort(sample_list))
