# coding=UTF-8
# 最长连续子串,并输出下标。

a = [3,4,5,3,2,0,6,7,8,5,4,7,8,9]
len_a = len(a)
xiabiao = {}


dic = {}
maxlen = 0
maxposl = 0
pos = 0
for i in a:
    if i not in dic:
        if (i-1 not in dic) and (i+1 not in dic):
            dic[i] = 1
            xiabiao[i] = []
            xiabiao[i].append(pos)

        if (i-1 in dic) and (i+1 not in dic):
            pre_len = dic[i-1]
            dic[i] = pre_len + 1
            dic[i-pre_len] = pre_len + 1
            xiabiao[i-pre_len].append(pos)
            
        if (i-1 not in dic) and (i+1 in dic):
            pre_len = dic[i+1]
            dic[i] = pre_len + 1
            dic[i+pre_len] = pre_len + 1
            xiabiao[i] = []
            xiabiao[i] = xiabiao[i+1][:]
            xiabiao[i].append(pos)

        if (i-1 in dic) and (i+1 in dic):
            pre_len_l = dic[i-1] 
            pre_len_r = dic[i+1]
            dic[i-pre_len_l] = pre_len_l + pre_len_r + 1
            dic[i+pre_len_r] = pre_len_l + pre_len_r + 1
            dic[i] = pre_len_l + pre_len_r + 1
            xiabiao[i-pre_len_l] = xiabiao[i-pre_len_l].append(pos) + xiabiao[i+pre_len_r]

        if dic[i] > maxlen:
            maxlen = dic[i]
            maxnuml = i - maxlen + 1
    pos = pos + 1
    
print "max len =", maxlen

print xiabiao[maxnuml]



