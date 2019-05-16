class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

        有效字符串需满足：

        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。

        示例 1:

        输入: "()"
        输出: true
        示例 2:

        输入: "()[]{}"
        输出: true
        示例 3:

        输入: "(]"
        输出: false
        示例 4:

        输入: "([)]"
        输出: false
        示例 5:

        输入: "{[]}"
        输出: true
        
        """
        a = []
        n = len(s)
        if n == 0:
            return 1
        for i in range(n):
            if len(a) == 0:
                a.append(s[i]) 
            else :
                if a[-1] == '(' and s[i] == ')':
                    del a[len(a)-1]
                elif a[-1] == '[' and s[i] == ']':
                    del a[len(a)-1]
                elif a[-1] == '{' and s[i] == '}':
                    del a[len(a)-1]
                else:
                    a.append(s[i])
        if len(a) == 0:
            return 1
        else:
            return 0
