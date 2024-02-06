#Bottom-Up DP

def maxSumAfterPartioning(arr, k):
    nums = len(arr)
    dp = [0] * nums

    for i in range(nums):
        max_val = 0

        for j in range(1,k+1, 1):
            if i - j + 1 >= 0:
                max_val = max(max_val, arr[i-j + 1])
                dp[i] = max(dp[i], (dp[i-j] if i-j >= 0 else 0) + max_val * j)
    return dp[-1]

