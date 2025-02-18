class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        left = 0
        max_l = 0
        n = len(s)

        for right in range(n):
            if s[right] not in s[left:right]:
                max_l = max(max_l,len(s[left:right]))
            while s[right] in s[left:right]:
                left += 1
        
        return max_l + 1
        