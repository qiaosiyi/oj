class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        数组内数字出现两次，或一次，找出出现一次的那个数字
        """
        a = 0
        for i in nums:
            a = a ^ i
        return a
