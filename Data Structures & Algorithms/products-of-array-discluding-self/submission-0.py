class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0]*n

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod*=nums[j]
            ans[i]=prod

        return ans