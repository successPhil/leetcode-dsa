from collections import defaultdict
#Initialize hashmap, left and right pointers
#To set up sliding window technique
#Add right pointer to char count
#Check window size - char_count[left]) <= k
# If not valid decrease char_count[left]
# Increment left pointer
# Update Answer


def charReplacement(s, k):
    left = right = ans = 0
    char_counts = defaultdict(int)
    max_freq = 0

    while right < len(s):
        char_counts[s[right]] += 1
        max_freq = max(max_freq, char_counts.get(s[right]))


        while right - left + 1 - max_freq > k:
            char_counts[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
        right+= 1
    return ans 



    


    #     while window_size - char_counts[left] >= k:
    #         char_counts[left] -= 1
    #         left += 1
    #     ans = max(ans, right - left + 1)
    #     right += 1
    # return ans

