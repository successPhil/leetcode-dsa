# Integer is in an array and represents the largest digit
# inputs:
# digits: List[int]

#outputs:
# rtype: List[int]


def plusOne(digits):
    string_nums = ""
    answer = []
    for num in digits:
        string_nums += str(num)



    string_to_int = int(string_nums)
    string_to_int += 1
    int_to_string = str(string_to_int)
    for integer in int_to_string:
        answer.append(int(integer))

    return answer



print(plusOne([9]))