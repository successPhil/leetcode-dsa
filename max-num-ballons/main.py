from collections import defaultdict
from collections import Counter
# Example 1:

# Input: text = "nlaebolko"
# Output: 1

# Example 2:

# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:

# Input: text = "leetcode"
# Output: 0

# Example 4:

# Input: text = "ballon"
# Output:: 0

# Example 5:

# Input" text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
# Output": 10


def maxNumberOfBalloons(text):
    #Get frequency of characters in "balloon"
    balloon_letters = Counter("balloon")
    #Initialize Counting dictionary for text
    counts = defaultdict(int)
    #Initialize ans to 0 as we cannot be sure the text will include enough chars for "balloon"
    ans = 0
    for letter in text:
        #Add only letters that can be found in "balloon" to our counting dictionary counts
        if letter in balloon_letters:
            counts[letter] += 1
            
    #Check that we got at least 5 unique characters (there are 5 distinct chars in "balloon")
    if len(counts.values()) < 5:
        return ans

#Decrease our counts by the letter matched with in balloon_letters
# Check if counts for that letter is still positive, return ans if not
# Increment answer each time we have finished iterating through "balloon"    
    while True:
        for letter in balloon_letters:
            counts[letter] -= balloon_letters[letter]
            if counts[letter] < 0:
                # return answer before it can be incremented
                return ans
        #Increment each time our for loop completes  
        ans += 1
print(maxNumberOfBalloons("nlaebolko"))
print(maxNumberOfBalloons("loonbalxballpoon"))
print(maxNumberOfBalloons("leetcode"))
print(maxNumberOfBalloons("ballon"))
print(maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))