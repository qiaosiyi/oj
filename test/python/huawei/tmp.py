while True:
    try:
        n = input()
    except:
        exit()
    
    a = bin(n)
    res = 0
    for i in a:
        if i == '1':
            res += 1
    print res