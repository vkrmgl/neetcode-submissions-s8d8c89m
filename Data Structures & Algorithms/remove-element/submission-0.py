class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cor = []
        for i in range(len(nums)):
            if nums[i]!=val:
                cor.append(nums[i])
        nums[:len(cor)]=cor
        return len(cor)