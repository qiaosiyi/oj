class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        """
        def next_num(tmp):
            res = ""
            i = 0
            tmp_n = len(tmp)
            while i < tmp_n:
                count = 1
                while i < tmp_n - 1 and tmp[i] == tmp[i+1]:
                    count += 1
                    i += 1
                res += (str(count) + tmp[i])
                i += 1
            return res
        res = "1"
        for i in range(1, n):
            res = next_num(res)
        return res
