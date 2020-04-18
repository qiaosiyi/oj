class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        给一个数组，求其中哪两个数字的和是给定值。返回两个数字的下标。
        使用字典，将数字和其下标保存在字典中。
        开始遍历，如果差值在字典中那么说明就是有，不在的话把当前值加入字典。
        这样每次新值和已经加入字典的值来做和，加入字典的序号是小的，所以输出时可以有固定的前后关系比较好处理。
        """
        lookup = {}
                   
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in lookup:
                return [lookup[tmp],i]
            lookup[nums[i]] = i
