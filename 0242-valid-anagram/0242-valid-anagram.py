class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -=1
        
        print(count)
        for value in count.values():
            if value != 0 :
                return False
        
        return True
        
        
        