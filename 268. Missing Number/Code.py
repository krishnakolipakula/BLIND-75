class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=n*(n+1)//2
        return res-sum(nums)




            
