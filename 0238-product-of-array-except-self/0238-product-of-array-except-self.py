class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n



            
        
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]

        
        suffix[-1] = nums[-1]  
        for i in range(n - 2, -1, -1):  
            suffix[i] = suffix[i + 1] * nums[i]
        
        suffix.reverse()

        print(nums)
        nums[0] = suffix[-2]
        nums[-1] = prefix[-2]
        print("********suffix***********")
        print(suffix)
        print("********refix***********")
        print(prefix)
        print("***************")
        print(nums)    
        print("***************")

        for i in range(len(nums)-2):
            print(prefix[i],suffix[len(nums) - 3 - i])
            nums[i+1] = prefix[i] * suffix[len(nums) - 3 - i]
        
        print(nums)
        return nums