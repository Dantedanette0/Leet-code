class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        occur = 0

        if not needle:
            return -1

        if needle == haystack:
            return 0
        
        if len(haystack) < len(needle):
            return -1





        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i




        if occur == 0:
            return -1
        else:
            return occur
        




        