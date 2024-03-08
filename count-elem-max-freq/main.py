#Inputs: nums --> List of nums

#Return: Integer, total number of elements with maximum frequency

#Approach

# Initialize ans to 0 to track number of elements with a maximum frequency
# Initialize max_frequency to 1 to track max frequency seen

# Create a hashmap to get number frequencies
# Update frequency for each letter while iterating through nums
# Update max_frequency to its current value or the current number frequency, whichever is greater

# Loop through hashmap frequencies and increment ans by frequency each time frequency == max_frequency


def countElementsMaxFrequency(nums):
    ans = 0
    max_frequency = 1

    number_frequencies = {}

    for num in nums:
        number_frequencies[num] = number_frequencies.get(num, 0) + 1
        max_frequency = max(max_frequency, number_frequencies.get(num))
    
    for frequency in number_frequencies.values():
        if frequency == max_frequency:
            ans += frequency
    return ans