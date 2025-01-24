class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dest = len(nums) - 1
        max_jumps = []
        i = 0
        while dest > 0:
            if i > len(nums) - 1:
                break

            if nums[i] + i  >=  dest:
               jump_amount =  nums[i]
               if jump_amount + i >= dest:
                    jump_amount = dest - i
               print(nums[i]) 
               print(f'jump, {jump_amount}')
               max_jumps.append(i)
               print(f'dest is, {dest}')
               dest = dest - jump_amount 
               i = 0
            else:
                i += 1
            
        print(max_jumps)
        return len(max_jumps)
