#you can only climb in steps of 1 and 2, so how many distinct steps are needed to climb n stairs?

class Solution:
    def climbStairs(self, n: int) -> int:
       stairs=[0]*(n+1)
       #print(stairs)
       stairs[1] = 1
       stairs[2] = 2
       for i in range(3,n+1):
           stairs[i] = stairs[i-1]+stairs[i-2]    #surprisingly, the sum of the previous 2 steps are it!

       return stairs[n]


"""
Runtime : 44ms
Beats 40.97%of users with Python3

Memory : 16.13MB
Beats 91.20%of users with Python3

"""
