class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        
        for number in nums2:
            nums1.append(number)
        
        nums1.sort()

        print(nums1)
        n = len(nums1)

        if n % 2 == 0:
            n = n//2
            n1 = nums1[n]
            n2 = nums1[n-1]
            return (n1+ n2)/2
        else:
            return nums1[n//2]

        return 0

        
        