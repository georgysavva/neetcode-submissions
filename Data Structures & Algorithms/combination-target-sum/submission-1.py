class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        state ={}
        all_paths = self.traverse(nums, target, state)
        unique_paths= set()
        for p in all_paths:
            p = tuple(sorted(p))
            unique_paths.add(p)
        result = [list(p) for p in unique_paths]
        return result
    def traverse(self, nums, target, state):
        if target==0:
            return [[]]
        if target < 0:
            return []
        if target in state:
            return state[target]
        result = []
        for num in nums:
            sub_paths = self.traverse(nums, target - num, state)
            sub_paths = [p + [num] for p in sub_paths]
            result.extend(sub_paths)
        state[target] = result
        return result