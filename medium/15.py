class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        for k in range(len(nums)):
            # Skip over repeated triplets.
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                triplet_sum = nums[i] + nums[j] + nums[k]
                if triplet_sum < 0:
                    i += 1
                elif triplet_sum > 0:
                    j -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    # Skip over any repeated triplets.
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    # Increment i and decrement j to move to next candidate
                    # triplet.
                    i += 1
                    j -= 1
        return triplets
