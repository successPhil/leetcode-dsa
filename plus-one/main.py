# Integer is in an array and represents the largest digit
# inputs:
# digits: List[int]

#outputs:
# rtype: List[int]

#Brute Force
# def plusOne(digits):
#     string_nums = ""
#     answer = []
#     for num in digits:
#         string_nums += str(num)

#     string_to_int = int(string_nums)
#     string_to_int += 1
#     int_to_string = str(string_to_int)
#     for integer in int_to_string:
#         answer.append(int(integer))

#     return answer

# lets do better

# def plusOne(digits):
#     number = int(''.join(list(map(str, digits))))
#     number += 1
#     return list(map(int, str(number)))


# math approach

def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n-1, -1, -1):
        digit_sum = digits[i] + carry
        digits[i] = digit_sum % 10
        carry = digit_sum // 10

    if carry:
        digits.insert(0, carry)
    return digits

