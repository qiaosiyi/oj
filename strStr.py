class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

        示例 1:

        输入: haystack = "hello", needle = "ll"
        输出: 2

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/implement-strstr
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        n = len(needle)
        m = len(haystack)
        if n == 0: return 0
        if n > m: return -1
        i = 0
        j = 0   
        flag = 0
        flag2= 0
        for k in range(m):
            if haystack[i] == needle[j]:
                if j == n - 1: 
                    return i - n + 1
                i = i + 1
                j = j + 1
                flag = 1
                if flag: flag2 = 1
            else :
                if flag2:
                    flag2 = 0
                    i = i - 1
                elif flag:
                    flag = 0
                    i = i + 1
                else:
                    i = i + 1
                j = 0
        return -1
