class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        k=min(len(word1),len(word2))
        print(k)
        output = ""

        for i in range(k):
            print(i)
            output += word1[i]+word2[i]
 
        if len(word1) > len(word2):
            output += word1[k:]
        if len(word2) > len(word1):
            output += word2[k:]

        return output

        