class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return  max(len(x) for x in ("".join([str(i) for i in nums]).split("0")))
