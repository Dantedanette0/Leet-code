class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        n = len(s)

        last_space = 0
        whitespaces = []
        last_char = 0

        if n == 0:
            return 0

        if n == 1 and s[0] != ' ':
            return 1
        if n == 1 and s[0] == ' ':
            return 0

        for i in range(n):
            if s[i] == " ":
                whitespaces.append(i)
            else:
                last_char = i
        
        print(whitespaces)
 

        last_space = 0
        for space in whitespaces:
            if space < last_char:
                last_space = space

        print(last_space)
        print(last_char)



        if (last_char == 0 or last_space == 0) and s[0] != ' ':
            return last_char - last_space + 1
        
        

        return last_char - last_space

        