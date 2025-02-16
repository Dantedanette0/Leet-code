class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        left = 0
        right = 0
        n = len(nums)
        window = nums[left:right]
        max = 0


        for i in range(n):
            if i == n - 1 and nums[i] == 1:
                right = i+1
                if nums[left] == 0:
                    left = i
                if max < len(nums[left:right]):
                    max = len(nums[left:right])

            if nums[i] == 1:
                right = i+1
                if nums[left] == 0:
                    left = i
            if nums [i] == 0:
                if max < len(nums[left:right]):
                    max = len(nums[left:right])
                left = i
                right = i
                
        return max

        