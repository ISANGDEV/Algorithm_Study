n=int(input())

total=[0] * n
print(total)
for i in range(n):
    if(i<=1):
        total[i]=1
    else:
        total[i]=total[i-2]+total[i-1]
print(total[n-1])
