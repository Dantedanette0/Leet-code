class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:


        occur = {}
        for num in arr:
            occur[num] = 1+ occur.get(num,0)

        
        print(occur)
        if len(occur.values()) == len(set(occur.values())):
            return True

        return False