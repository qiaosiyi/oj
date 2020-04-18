class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

        最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

        你可以假设除了整数 0 之外，这个整数不会以零开头。

        示例 1:

        输入: [1,2,3]
        输出: [1,2,4]
        解释: 输入数组表示数字 123。
        """
        n = len(digits)
        s = 0
        shi = 1
        for i in range(n):
            s = s + shi*digits[n-1-i]
            shi = shi*10
        s = s + 1
        rlist = []
        while s :
            a = s % 10
            rlist.append(a)
            s = s / 10
        m = len(rlist)
        rrlist = []
        for i in range(m):
            rrlist.append(rlist[m-1-i])
        return rrlist
        
