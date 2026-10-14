class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
    
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in res:
                return[res[remaining],i]
            res[nums[i]]=i
        return res

        