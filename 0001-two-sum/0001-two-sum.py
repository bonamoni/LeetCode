class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(0,n):
            a = nums[i]
            b = target-a
            if(b in d):
                return[i,d[b]]
            d[a] = i
