class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []
        new = newInterval

        for inter in intervals:
            if inter[1] < newInterval[0] or inter[0] > newInterval[1]:
                output.append(inter)
        
        for inter in intervals:
            if inter not in output:
                new[0] = min(newInterval[0],inter[0])
                new[1] = max(newInterval[1],inter[1])


        output.append(new)
        output.sort()
        return output
        