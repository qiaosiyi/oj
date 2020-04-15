import random
random.seed(4)
n=10000000
cnt=0
for i in range(n): 
    arr=[0]*12
    for j in range(10):
        rnd=random.randint(0,11)
        arr[rnd]+=1
    cnt0=0 
    for j in range(12):
        if arr[j]==0:
            cnt0+=1
    if cnt0==10:
        cnt+=1
print(cnt/n)