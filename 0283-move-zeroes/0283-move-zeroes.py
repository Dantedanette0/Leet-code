class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes = 0
        for num in nums:
            if num == 0:
                num_zeroes += 1
        for i in range(num_zeroes):
            nums.remove(0)
            nums.append(0)




        