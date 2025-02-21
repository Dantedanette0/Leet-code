class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        words = []
        word = ""
        comb = {}

        for i in range(len(s)):

            if s[i] == " " or i == len(s) - 1:
                if i == len(s) - 1:
                    word += s[i]
                words.append(word)
                word = ""
            if s[i] != " ":
                word += s[i]

        print(words)

        if len(pattern) != len(words):
            print("wierd len")
            return False


        for char,word in zip(pattern,words):
            if char in comb:
                if comb[char] != word:
                    return False
            elif word in comb.values():
                return False
            
            comb[char] = word

        

        

        return True



        
        