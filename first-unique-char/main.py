#inputs: s:string
#return: integer

#We need to loop through our string and get a count of our chars
# We then can loop through our string and return the first letter with a count = 1
# If that condition is never met we can return -1 because it was not found


def firstUniqChar(s):
    char_counts = {}

    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    

    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
    return -1

#Initial approach


#using count to check for frequencies as we loop through input

#Note that initial solution has a better runtime than using count() like this

# Here we have the case where for iteration of our loop through our string, another loop is performed to return the count() value
# In cases where a solution (unique char) is in the beginning of the list, this will run faster
# But if a solution is not present, we must perform O(n^2) steps to check a number has not been found


# def firstUniqChar(s):
#     for i in range(len(s)):
#         if s.count(s[i]) == 1:
#             return i
#     return -1

