class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        fuel = 0
        sum_fuel = 0
        index = 0

        for i in range(len(gas)):

            current_gas = gas[i] - cost [i]

            fuel += current_gas
            sum_fuel += current_gas

            if fuel < 0 :
                fuel = 0
                index = i+ 1
                

        
        if sum_fuel < 0:
            return -1
        else:
            return index
        
        