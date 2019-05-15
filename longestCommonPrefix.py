class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        编写一个函数来查找字符串数组中的最长公共前缀。

        如果不存在公共前缀，返回空字符串 ""。

        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"
        示例 2:

        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。
        说明:

        所有输入只包含小写字母 a-z 。
        """
        a=""
        n = len(strs)
        j = 0
        f = 1
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in strs:
            if i == "":
                return ""
        m = 999999999999
        for i in strs:
            if len(i)<m:
                m = len(i)
        
        for k in range(m):
            for i in range(n-1):
                if strs[i][j] == strs[i+1][j]:
                    f = 1
                else:
                    f = 0
                    break
            if f:
                a = a + strs[0][j]
                j = j + 1
        return a
