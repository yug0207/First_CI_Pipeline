def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4]
    print("Sum:", sum_of_list(sample_numbers))
