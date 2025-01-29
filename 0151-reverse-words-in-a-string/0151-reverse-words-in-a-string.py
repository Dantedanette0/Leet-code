class Solution:
    def reverseWords(self, s: str) -> str:


        
        s = s[::-1]

        output = []
        left = 0

        for right in range(len(s) + 1): 

            if right == len(s) or s[right] == ' ':

                if left < right:
                    output.append(''.join(reversed(s[left:right])))
                left = right + 1 
        
        return ' '.join(output) 





        