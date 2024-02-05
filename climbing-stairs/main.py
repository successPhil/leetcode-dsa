# It takes n steps to reach the top

# We can take 1 step or 2 steps at a time to get to the top

# How many distinct ways can you climb to the top

#step + step = (individual single steps)
# step + 2 step = (individual plus double step)
# 2 step + step = (individual)

#n = 4
# 1 step + 1 step + 2
# 1 + 1 + 1 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 2 step + 1 step


# def climbStairs(n):
#     if n <= 2:
#         return n
    
# #Initialize an array to store the number of ways for each step

#     dp = [0] * (n + 1)

#     #Base cases
#     dp[1] = 1
#     dp[2] = 2

#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i-2]

#     return dp[n]

def climbStairs(n):
    return n * ( n +1 /2)

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))

  