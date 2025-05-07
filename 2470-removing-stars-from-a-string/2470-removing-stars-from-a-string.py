class Solution:
    def removeStars(self, s: str) -> str:

        n = len(s) - 1

        stars = 0 

        while n >= 0:
 

            if s[n] == '*':
                stars += 1
                s = s[:n] + s[n+1:]

            elif s[n] != '*' and stars > 0:
                #remove s[n]
                s = s[:n] + s[n+1:]
                stars -= 1

            n -= 1
        print(stars)
        return s
        