# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse_string(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_string(["h","e","l","l","o"]))
