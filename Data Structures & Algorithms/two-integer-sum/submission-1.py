class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {n:i for i,n in enumerate(nums)}
        for i,n in enumerate(nums):
            j = table.get(target-n)
            if j is not None and j!=i:
                return [i,j]
