class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_candies = max(candies)

        output = []

        print(max_candies)

        for cand in candies:
            if cand + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)

        return output
        