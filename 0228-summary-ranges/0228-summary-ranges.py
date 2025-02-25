class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]

        output = []
        start = nums[0]


      

        for i in range(1,n+1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    output.append(str(start))
                else:
                    output.append(f"{start}->{nums[i - 1]}")              
                if i < n:
                    start = nums[i]


  


            

        return output
