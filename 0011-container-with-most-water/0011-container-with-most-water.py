class Solution:
    def maxArea(self, height: List[int]) -> int:

       


        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        max_water = min(left_max,right_max) * (right - left)

        while left < right:

            if left_max < right_max:
                 left+=1
                 left_max = height[left]
                 if max_water < min(left_max,right_max) * (right - left):
                    max_water = min(left_max,right_max) * (right - left)
            else:
                right -=1
                right_max = height[right]
                if max_water < min(left_max,right_max) * (right - left):
                    max_water = min(left_max,right_max) * (right - left)
           
            

        return max_water
        