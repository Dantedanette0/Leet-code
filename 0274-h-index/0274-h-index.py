class Solution:
    def hIndex(self, citations: List[int]) -> int:


        max_h_index = 0

        citations.sort(reverse = True)
        for i in range(len(citations)):
            h_index = i + 1
            if h_index <= citations[i]:
                max_h_index = h_index

        return max_h_index

        
        