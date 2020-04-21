# coding=UTF-8
# Largest Rectangle in Histogram And 85. Maximal Rectangle
# 求一系列矩形图内邻接矩形的最大面积。
# 
# 这道题使用的知识点是：栈
# 从左到右，如果当前对应的小矩形高度大于栈顶对应小矩形高度，进栈，移动到下一个小矩形
# ，，，，，，，，，
# 否则栈顶元素出栈，再次比较此时栈顶元素和当前对应的小矩形高度，如果前者还是大于后者，
# 继续出栈，直到小于等于为止
# 依次计算上面一次连续出栈的小矩形组成的矩形面积，最大面积依此不断更新
# 最后返回最大面积
# 注意：这里每次进栈的是小矩形对应的索引而不是其高度，同时可以看到stack中索引对应的高度始终是递增的


heights = [2,1,5,6,3,2]

# a.append(0)
# stack = []
# i = 0
# maxre = 0
# h = 0

# while i < len(a):
#     newnum = a[i]
#     if not stack:
#         stack.append(i)
#         i += 1
#     elif newnum > stack[-1]:
#         stack.append(i)
#         i += 1
#     else:
#         h = a[stack[-1]]
#         maxre = max(maxre,h*(i-stack[-1]))
#         stack.pop()

#     print "h =",h,"i-stack[-1]) =",i-stack[-1],"i =",i,"max = ",maxre,"newnum =",newnum

# print "max =", maxre


      
heights.append(0)
stack = []
i = 0
result = 0
while i<len(heights):
    if not stack or heights[stack[-1]]<heights[i]:
        stack.append(i)
        i+=1
    else:
        num = stack.pop(-1)
        result = max(result,heights[num]*(i-stack[-1]-1 if stack else i)) #三元表达式，if stackj
print result










