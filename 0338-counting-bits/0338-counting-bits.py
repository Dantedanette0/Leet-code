class Solution:
    def countBits(self, n: int) -> List[int]:
        output =[]
        def  countSetBits(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count
        for i in range(n+1):
            output.append(countSetBits(i))
        return output
        