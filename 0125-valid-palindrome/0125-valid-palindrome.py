class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = ''.join([char for char in s if char.isalnum()]).lower()
        print(s)

        left = 0
        right = len(s) - 1
        pal = True

        while left < right:

            if s[left] != s[right]:
                pal = False
                break
            left += 1
            right -= 1



        return pal

        