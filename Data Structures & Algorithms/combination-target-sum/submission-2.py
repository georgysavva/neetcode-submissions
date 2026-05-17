class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        state ={}
        all_paths = self.traverse(nums,0, target, state)
        return all_paths
    def traverse(self, nums, start, target, state):
        if target==0:
            return [[]]
        if target < 0:
            return []
        if target in state:
            return state[(target,start)]
        result = []
        for i in range(start, len(nums)):
            num = nums[i]
            sub_paths = self.traverse(nums, i, target - num, state)
            sub_paths = [p + [num] for p in sub_paths]
            result.extend(sub_paths)
        state[(target, start)] = result
        return result