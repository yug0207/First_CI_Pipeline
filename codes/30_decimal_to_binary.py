def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number must be non-negative")
    if number == 0:
        return "0"
    bits = []
    temp = number
    while temp > 0:
        bits.append(str(temp % 2))
        temp //= 2
    bits.reverse()
    return "".join(bits)

if __name__ == "__main__":
    sample_num = 10
    print("Binary:", decimal_to_binary(sample_num))
