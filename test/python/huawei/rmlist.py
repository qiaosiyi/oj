# coding=UTF-8
# 有一个数组a[N]顺序存放0~N-1，要求每隔两个数删掉一个数，
# 到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。
# 以8个数(N=7)为例:｛0，1，2，3，4，5，6，7｝，0->1->2(删除)->3->4->5(删除)->6->7->0(删除),
# 如此循环直到最后一个数被删除。


while True:
    try:
        n = input() 
    except:
        exit()
    class node:
        def __init__(self, num = None, next = None):
            self.num = num
            self.next = next
        def __str__(self):
            return "%d" % self.num
    listn = []
    for i in range(n):
        listn.append(node(i))

    for i in range(n - 1):
        listn[i].next = listn[i+1]
    listn[n - 1].next = listn[0]

    # for i in listn:
    #     print i,
    # print

    lenlist = n
    root = node(99)
    root.next = listn[0]
    i = 0
    head = root
    nextn = node()

    while lenlist>2:
        if i < 2:
            head = head.next
            i += 1
            # print head
        else:
            i = 0
            nextn = head.next

            head.next = nextn.next
            # print "rm",nextn
            lenlist -= 1


    # print "output:",head
    print head.next.next

