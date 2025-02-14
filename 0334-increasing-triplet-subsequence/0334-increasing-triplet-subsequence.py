class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for number in nums:
            if number <= first:
                first = number
            elif number <= second:
                second = number
            else:
                return True
            
  


        return False
        