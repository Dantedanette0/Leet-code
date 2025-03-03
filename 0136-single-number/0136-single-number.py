class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occur = {}

        for number in nums:
            occur[number] = 1 + occur.get(number,0)

        print(occur)
        for x in occur:
            if occur[x] == 1:
                return x
        return 0
        