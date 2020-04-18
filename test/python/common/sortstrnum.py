###
    分类排序，字母排列字母，数字排序数字，结果的位置不能变
    input：sd98f7a90s8df876as896d5f67a5123
    output：aa01a2d35d5df666ff777s8s88s8999
###

line2 = "sd98f7a90s8df876as896d5f67a5123"


def isstr(a):
        if a <= 'z' and a >= 'a':
                return 1
        else:
                return 0

#def isnum(a):
#       if a <= '9' and a >= '0':
#               return 1
#       else:
#               return 0
strlist = []
numlist = []

index = []
for i in line2:
        if isstr(i):
                strlist.append(i)
                index.append(1)#is a char
        else:
                numlist.append(i)
                index.append(0)#is a number
strlist.sort()
numlist.sort()
res = ""
for j in index:
        if j :
#               res.append(strlist[0])
                res = res + strlist[0]
                strlist.pop(0)
        else:
#               res.append(numlist[0])
                res = res + numlist[0]
                numlist.pop(0)
print line2
print res
