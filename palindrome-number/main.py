def say_hello():
    return "hello"


# def isPalindrome(x):
    
#     if x < 0:
#         return False
#     num_str = str(x)
#     left = 0
#     right = len(num_str)-1
#     while left < right:
#         if num_str[left] != num_str[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

def isPalindrome(x):
    if x < 0:
        return False
    
    original_num = x
    reversed_num = 0
    
    while x > 0:
        trail = x % 10
        reversed_num = reversed_num * 10 + trail
        x //= 10
    return original_num == reversed_num





    