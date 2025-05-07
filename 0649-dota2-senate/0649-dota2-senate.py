class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        radiant = []
        dire = []
        i = 0
        length = len(senate)

        while i < length:
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
            i = i + 1
        
        while len(radiant) > 0 and len(dire) > 0:
            # dequeue the first Radiant
            r_index = radiant[0]
            del radiant[0]
            # dequeue the first Dire
            d_index = dire[0]
            del dire[0]

            if r_index < d_index:
                radiant.append(r_index + length)
            else:
                dire.append(d_index + length)

            



        if len(radiant) > 0:
            return "Radiant"
        else:
            return "Dire"
        