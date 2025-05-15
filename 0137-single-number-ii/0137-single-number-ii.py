class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        n = len(nums)
        
        nums.sort()

        index = 0

        while index < n-2:
            if nums[index] != nums[index+1]:
                return nums[index]
                
            index += 3
        
        return nums[-1]
