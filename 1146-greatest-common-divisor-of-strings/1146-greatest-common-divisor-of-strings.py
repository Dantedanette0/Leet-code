class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if  str1+str2 != str2+str1: return ''

        n1=int(len(str1))
        n2=int(len(str2))

        while(n1 !=0 and n2 !=0):
            if n1>n2: n1=n1%n2
            else: n2=n2%n1
        return str1[:int(n1)] if n1!=0 else str1[:int(n2)]
       


        