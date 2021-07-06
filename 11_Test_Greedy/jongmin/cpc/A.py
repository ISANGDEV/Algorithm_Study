T=int(input())
twice=[0,2,4,6,8,10,12,14]
for _ in range(T):
    num=list(map(int,list(input())))
    for i in twice:
        num[i]=num[i]*2
        if(num[i]>=10):
            num[i]=num[i]//10+num[i]%10
    result=sum(num)
    if(result%10==0):
        print('T')
    else:
        print('F')
