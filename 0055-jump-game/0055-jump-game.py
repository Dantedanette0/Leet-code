class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        destination = len(nums) -1

        if len(nums) < 2:
            return True
        if len(nums) == 1 and nums[0] == 0:
            return False

        if not(0 in nums):
            return True
        
        index_of_zeros = [0]

        for i in range (len(nums)):
            if nums[i] == 0:
                index_of_zeros.append(i)
        checker = []  

        for i in range(len(index_of_zeros)):
            check = nums[:index_of_zeros[i]]
            for i_c in range(len(check)):
                if nums[-1] == 0 and i == len(index_of_zeros)-1 :

                    if i_c + check[i_c] >=index_of_zeros[i]:
                        checker.append(i_c)
                        break;
                if i_c + check[i_c] >index_of_zeros[i]:
                    checker.append(i_c)
                    break;

        print(checker) 
        print(index_of_zeros)
        if len(checker) == len(index_of_zeros) -1:
            return True
        
        return False



