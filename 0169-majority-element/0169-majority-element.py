class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return null
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        n = len(nums)
        n = n/2
        n = int(n)
        majority = 0
        counter = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                counter += 1
                if counter == n:
                    majority = nums[i]
                    return majority
            else:
                counter = 0


    
        