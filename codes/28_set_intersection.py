def set_intersection(first, second):
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    return result

if __name__ == "__main__":
    first_set = {1, 2, 3}
    second_set = {2, 3, 4}
    print("Intersection:", set_intersection(first_set, second_set))
