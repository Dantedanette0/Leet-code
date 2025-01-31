class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        nums_map = {}
        n = len(nums)

        for i in range(n):
            nums_map[nums[i]] = i


        for i in range(n):
            complement = target - nums[i]
            if nums[i] in nums_map and complement in nums_map and  nums_map[complement] != i:
                return [i, nums_map[complement]]

        print(numMap)

        
        


           
      
        print(output)
        print(nums)
        
  
        
  
        
        

        return []

        