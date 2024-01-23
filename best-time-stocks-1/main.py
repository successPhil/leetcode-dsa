# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5


# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0

def maxProfit(prices):
    ans  = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        ans = max(ans, price - lowest)
    return ans


# def maxProfit(prices):
#     left = right = profit = 0
#     lowest = prices[0]

#     while right < len(prices):

#         while lowest > prices[right]:
#             lowest = prices[right]
#             left = right
#         profit = max(profit, prices[right] - prices[left])
#         right += 1
#     return profit


  




print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))