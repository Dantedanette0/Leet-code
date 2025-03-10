class Solution:
    def tribonacci(self, n: int) -> int:

        prev1 = 0
        prev2 = 1
        next = 1

        for i in range(n):
            prev1,prev2,next = prev2,next,prev1+prev2+next
        
        return prev1


        