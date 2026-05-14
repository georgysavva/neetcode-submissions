class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search(nums, target, 'left')
        right = self.search(nums, target, 'right')
        return [left, right]
    def search(self, nums, target, direction):
        l = 0
        r = len(nums) -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                if direction=='right':
                    if mid + 1 <= r:
                        if nums[mid + 1] == target:
                            l = mid + 1
                        else:
                            return mid
                    else:
                        return mid
                else:
                    if mid - 1 >= l:
                        if nums[mid - 1] == target:
                            r = mid - 1
                        else:
                            return mid
                    else:
                        return mid
            elif target<nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        return -1