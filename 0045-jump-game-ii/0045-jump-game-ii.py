class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        maxReach = 0
        currReach = 0
        jumps = 0
        
        for i in range(n - 1): 
            maxReach = max(maxReach, i + nums[i])
            
            if i == currReach:
                jumps += 1
                currReach = maxReach
                
                if currReach >= n - 1:
                    break
                    
        return jumps