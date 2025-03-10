class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n
        
        prev = 2
        next = 3

        for i in range(n-2):
            prev,next = next,prev+next
        
        return prev

