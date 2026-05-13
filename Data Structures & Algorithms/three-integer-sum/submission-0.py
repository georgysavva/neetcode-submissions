class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        results = set()
        for i in range(len(nums)-2):
            j = i +1
            k = len(nums)-1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    results.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    j+=1
                    k-=1
        results = [list(t) for t in results]
        return results

