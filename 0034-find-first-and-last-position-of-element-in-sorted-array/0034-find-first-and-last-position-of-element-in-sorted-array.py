class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        out = [-1,-1]
        if n == 0:
            return out
        
        for i in range(n):
            if nums[i] == target:
                out[0] = i
                out[1] = i
                break


        if n == 1:
            return out
        

        index = out[0] + 1
        if index  < n :
            while index < n:
                if nums[index] == target:
                    out[1] = out[1] + 1
                
                index += 1
        return out
        