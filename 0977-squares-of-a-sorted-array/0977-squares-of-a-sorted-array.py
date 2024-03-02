class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, key=abs)
        return [pow(i, 2) for i in nums]