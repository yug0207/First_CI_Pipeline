def rotate_list(items, k):
    if not items:
        return []
    n = len(items)
    shift = k % n
    if shift == 0:
        return list(items)
    return list(items[-shift:] + items[:-shift])

if __name__ == "__main__":
    sample_items = [1, 2, 3, 4, 5]
    print("Rotated list:", rotate_list(sample_items, 2))
