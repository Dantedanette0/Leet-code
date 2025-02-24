class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False
        
        map1 = {}
        for char in word1:
            map1[char] = 1+ map1.get(char,0)

        map2 = {}
        for char in word2:
            map2[char] = 1+ map2.get(char,0)

        map1 = dict(sorted(map1.items(), key=lambda item: item[1]))
        map2 = dict(sorted(map2.items(), key=lambda item: item[1]))
        print(map1)
        print(map2)
        if list(map1.values()) == list(map2.values()):
            return True

        return False
        