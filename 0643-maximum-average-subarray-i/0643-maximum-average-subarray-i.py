class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        current = sum(nums[:k]) 
        max = current

        for i in range(k,n):
            current += (nums[i] - nums[i-k]) 
            if max < current:
                print(max)
                max = current
        
        return max/k

        