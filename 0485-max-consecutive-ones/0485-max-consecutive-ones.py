class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        left = 0
        right = 0
        n = len(nums)
        max_c = 0


        for i in range(n):
            if nums[i] == 0:
                left = right +1
                right = left
            
            diff = right - left 
            if left == 0:
                diff += 1
            right += 1
            max_c = max(max_c,diff) 
        
        return max_c

        