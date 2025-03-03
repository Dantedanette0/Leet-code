class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = []
        right = []
        cl = 0
        cr = sum(nums)

        for i in range(len(nums)):
            left.append(cl)
            cr -= nums[i]
            cl += nums[i]
            
  
            right.append(cr)

           
 
  
        print(left)
        print(right)

        for i in range(len(left)):
            if left[i] == right[i]:
                return i

        return -1
            

        