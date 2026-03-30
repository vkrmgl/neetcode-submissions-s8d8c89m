class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i==j:
                    pass
                else:
                    total*=nums[j]
            ans.append(total)
        return ans