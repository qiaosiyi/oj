class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

        如果不存在最后一个单词，请返回 0 。

        说明：一个单词是指由字母组成，但不包含任何空格的字符串。

        示例:

        输入: "Hello World"
        输出: 5

        """
        if s=='':
            ans=0
        elif s.isspace():
            ans=0
        else:
            s=s.split()
            ans=len(s[-1])
        return ans
