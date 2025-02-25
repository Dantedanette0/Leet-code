class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        n = len(intervals)
        output = []

        for i in range(n):
            curr = intervals[i]

            if not output or output[-1][1] < curr[0]:
                output.append(curr)
            else:
                output[-1][1] = max(curr[1],output[-1][1])
            

    
        return output
                

        