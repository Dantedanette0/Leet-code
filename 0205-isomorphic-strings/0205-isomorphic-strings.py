class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 

        hash_s = {}
        hash_t = {}
        comp_map = {}
        if len(s) != len(t):
            return False

        for schar,tchar in zip(s,t):
            if schar in comp_map:
                if comp_map[schar] != tchar:
                    return False
            elif tchar in comp_map.values():
                return False

            comp_map[schar] = tchar

        print(comp_map)    
        return True

        