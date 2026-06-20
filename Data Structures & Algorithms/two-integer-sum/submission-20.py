class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,num in enumerate(nums):
            lookFor = target - num
            if lookFor in res:
                return [res[lookFor], i]
            res[num] = i
        