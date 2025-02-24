class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [[],[]]

        for number in nums1:
            if number not in nums2 and number not in output[0]:
                output[0].append(number)
        
        for number in nums2:
            if number not in nums1 and number not in output[1]:
                output[1].append(number)

        return output

        