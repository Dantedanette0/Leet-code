class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i_s = 0
        i_t = 0

        if s == "":
            return True
        if t == "":
            return False

        while i_t < len(t):
            
            if s[i_s] == t[i_t]:
                print("happened")
                i_s+=1
                if i_s > len(s)-1:
                    return True

            i_t += 1

        return False

        