class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            current_sum = None
            while i < j and current_sum != target:
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(current_sum - target) < abs(best - target):
                    best = current_sum
                if current_sum < target:
                    i += 1
                elif current_sum > target:
                    j -= 1
        return best
