class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and num + num == target:
                return [index_map[num], i]
            index_map[num] = i
        for num in nums:
            if num + num != target and target - num in index_map:
                return [index_map[num], index_map[target - num]]
        return None
