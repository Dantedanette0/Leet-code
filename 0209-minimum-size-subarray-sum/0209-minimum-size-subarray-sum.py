class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left = 0
        sum = 0
        min_l = float("inf")

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                if right - left + 1 < min_l:
                    min_l = right - left + 1
                sum -= nums[left]
                left += 1


        if min_l == float("inf"):
            return 0
        return min_l


        