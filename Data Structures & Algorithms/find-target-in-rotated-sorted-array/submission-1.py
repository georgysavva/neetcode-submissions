class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        break_index=-1
        while l!=r:
            mid = (l+r)//2
            print("l mid r", l, mid, r)
            if mid == l:
                break_index=r
                break
            if nums[l] < nums[mid] and nums[mid] < nums[r]:
                break_index=l
                break
            if nums[l]> nums[mid]:
                r = mid
            else:
                l=mid
        print('break', break_index)
        left_segment = nums[:break_index]
        right_segment = nums[break_index:]
        print('left seg', left_segment)
        print('right seg', right_segment)
        target_i = self.bin_search(left_segment,target)
        print('left target i', target_i)
        if target_i == -1:
            target_i=self.bin_search(right_segment,target)
            if target_i == -1:
                return -1
            
            target_i = len(left_segment) + target_i
            print('right target i', target_i)

        return target_i
    def bin_search(self,nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid +1
        return -1
