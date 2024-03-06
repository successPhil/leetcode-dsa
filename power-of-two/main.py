

#Inputs: Int
# Return: Bool

# Want to check that 2 raised to a power, is equal to n

# def isPowerOfTwo(n):
#     if n < 1:
#         return False
#     power = 1
#     while power < n:
#         power *= 2
#     return power == n


## Bitwise comparison


def isPowerOfTwo(n):
    return n > 0 and n & (n-1) == 0