class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = set(nums)
        if len(nums) == len(num):
            return False
        else:
            return True
