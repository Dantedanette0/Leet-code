class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        r = n-1
        l = 0
        print(nums)
        counter = 0
        while l < r:
            curr = nums[l] + nums[r]
            if  curr == k:
                counter += 1
                l += 1
                r -= 1
            if curr < k :
                l+=1
            if curr > k:
                r -= 1

        
        return counter
        