class Solution:
    def candy(self, ratings: List[int]) -> int:
    
        candy = [1] * len(ratings)

        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candy[i + 1] = candy[i] + 1


        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy[i - 1] = max(candy[i - 1], candy[i] + 1)


        print(candy)
        return sum(candy)



        