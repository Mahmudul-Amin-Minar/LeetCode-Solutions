def reverseBits(n: int) -> int:
    reversed_bits_result = 0
    for _ in range(32):
        reversed_bits_result = (reversed_bits_result << 1) + (n & 1)
        n = n >> 1
    return reversed_bits_result

print(reverseBits(19))