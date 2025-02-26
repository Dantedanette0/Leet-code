class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)
        k = 0
        s = []
        s.append(chars[0])
        counter = 0
        s_counter = ""

        for i in range(n):
            if chars[k] == chars[i]:
                counter += 1
            if chars[k] == chars[i] and i == n-1:
                if counter > 1:
                    s_counter = str(counter)
                    for char in s_counter:
                        s.append(char)

            if chars[k] != chars[i]:
                if counter > 1:
                    s_counter = str(counter)
                    for char in s_counter:
                        s.append(char)
               
                s.append(chars[i])
                counter = 1
                k = i
            
        print(s)
        chars[:len(s)+1] = s
        print(chars)
        return len(s)

            


  
        
        