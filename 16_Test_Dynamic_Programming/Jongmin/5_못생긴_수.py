n=int(input())
dp=[False, True]
i=2
cnt=1
primefactor=[2,3,5]
while cnt<n:
    status=False
    for j in primefactor:
        if(i%j==0 and dp[i//j]==True):
            status=True
            cnt+=1
            break
    dp.append(status)
    i+=1
print(len(dp)-1)
