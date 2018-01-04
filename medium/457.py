class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in xrange(len(nums)):
            if self.found_loop(nums, i):
                return True
        return False

    def found_loop(self, nums, i):
        """Returns True if there exists a forward or backward loop from i."""
        current = i
        direction = 1 if nums[i] > 0 else -1
        for step in xrange(len(nums)):
            if nums[current] * direction < 0 or abs(nums[current]) == len(nums):
                return False
            current = (current + nums[current]) % len(nums)
        return True
