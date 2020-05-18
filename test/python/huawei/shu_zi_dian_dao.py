while True:
    try:
        n = input()
    except:
        exit()
    
    data = []
    for i in range(n):
      data.append([])
    s = 1
    k = 1
    for i in range(n):
        for j in range(s):
            data[i].append(k)
            k += 1
        s += 1
    s = 0
    k = n
    l = 0
    # print data
    for i in range(n):
        for j in range(k):
            print data[l+j][-1 - i],
        k -= 1
        l += 1
        print