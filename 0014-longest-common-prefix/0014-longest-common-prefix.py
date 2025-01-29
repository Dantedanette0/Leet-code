class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = ""
        first_str=min(strs, key=len)


        for i in range(len(first_str)):

            for j in range (len(strs)):

                check = strs[j]
                if first_str[i] != check[i]:
                    return lcp;
    
                
                if j == len(strs) - 1:
                    print("ya")
                    lcp += first_str[i]
            

        return lcp

        