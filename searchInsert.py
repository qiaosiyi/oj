class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

        你可以假设数组中无重复元素。

        示例 1:

        输入: [1,3,5,6], 5
        输出: 2

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/search-insert-position
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if target <= nums[0]: return 0
        if target == nums[-1]: return len(nums)-1
        if target > nums[-1]: return len(nums)
        maxn = len(nums)
        minn = 0
        while maxn - minn > 1:
            if target < nums[(maxn + minn)/2]:
                maxn = (maxn + minn)/2
            elif target > nums[(maxn + minn)/2]:
                minn = (maxn + minn)/2
            else:
                return (maxn + minn)/2
        return minn+1
