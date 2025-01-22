class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #len(nums - k) is the number of elements that needs to be moved k times
        n = len(nums)
        k = k % n
        if k > 0:
            nums.reverse()
            if n >= 3 :
                start_1 = 0
                end_1 = k
                nums[start_1:end_1] = reversed(nums[start_1:end_1])
                nums[end_1:] = reversed(nums[end_1:])
        
        
        