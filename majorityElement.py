class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        数组中，个数大于二分之一总数的那个数字，遇到一样的+1 不一样的-1 并且更换基准数字，最后剩下的基准数字肯定是众数
        """
        count = 1
        a = nums[0]
        for i in range(len(nums)-1):
            if a == nums[i + 1]:
                count = count + 1
            else:
                count = count - 1
            if count == 0:
                a = nums[i + 2]
        return a
