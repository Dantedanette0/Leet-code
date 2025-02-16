class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowel = ['a', 'e', 'i', 'o','u']
        max_v = 0
        window = s[:k]
        n = len(s)

        for char in window:
            if char in vowel:
                max_v+=1
        
        current_v = max_v

        for i in range(k,n):
            if s[i] in vowel:
                current_v += 1
            if s[i-k] in vowel:
                current_v -= 1
            if current_v > max_v:
                max_v = current_v

        return max_v