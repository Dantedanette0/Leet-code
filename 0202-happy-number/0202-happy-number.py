class Solution:
    def isHappy(self, n: int) -> bool:
        digit_map = {
            "0": 0,
            "1": 1,
            "2": 4,
            "3": 9,
            "4": 16,
            "5": 25,
            "6": 36,
            "7": 49,
            "8": 64,
            "9": 81,
        }
        
        while n != 4:

            str_num = str(abs(n))
            
            n = sum(digit_map[digit] for digit in str_num)

            if n == 1:
                return True

        return False



        