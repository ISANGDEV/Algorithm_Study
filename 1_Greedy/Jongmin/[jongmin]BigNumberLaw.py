N,M,K=map(int, input().split())
numlist=list(map(int, input().split()))
numlist.sort(reverse=True)
result=0
cnt=0
for i in range(1,M+1):
    if(i%(K+1)==0):
        result+=numlist[1]
    else:
        result+=numlist[0]
print(result)