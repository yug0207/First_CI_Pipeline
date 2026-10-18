def find_max_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

if __name__ == "__main__":
    sample_numbers = [4, 9, 1, 7]
    print("Max and Min:", find_max_min(sample_numbers))
