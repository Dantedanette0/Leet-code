class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        n = len(intervals)

        intervals.sort(key=lambda x: x[1])
        output = 0
        i = 0
        print(intervals)
        while i < len(intervals)-1:

            curr = intervals[i]
            next = intervals[i+1]
            if curr[1] > next[0]:
                intervals.remove(next)
                output +=1
            else:
                i+=1


            
            
            


        print(intervals)
            

        

        return output

        