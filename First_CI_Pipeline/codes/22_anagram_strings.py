def is_anagram(first, second):
    clean_first = "".join(char.lower() for char in first if not char.isspace())
    clean_second = "".join(char.lower() for char in second if not char.isspace())
    if len(clean_first) != len(clean_second):
        return False
    char_counts = {}
    for char in clean_first:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in clean_second:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] < 0:
            return False
    return True

if __name__ == "__main__":
    first_str = input("Enter first string: ")
    second_str = input("Enter second string: ")
    print("Is anagram:", is_anagram(first_str, second_str))
