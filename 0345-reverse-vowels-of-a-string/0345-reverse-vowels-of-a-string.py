class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set('aeiouAEIOU')  
        n = len(s)
        aoti = []


        for char in s:
            if char in vowels:
                aoti.append(char)

        aoti.reverse() 
        print(aoti)
        s_v = []
        k=0

        for char in s:
            if char in vowels:
                s_v.append(aoti[k]) 
                k += 1
            else:
                s_v.append(char) 

        return ''.join(s_v) 

 
            
        



        