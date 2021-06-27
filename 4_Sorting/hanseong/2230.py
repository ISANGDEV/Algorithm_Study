n, m= map(int, input().split())

total=[]
for i in range(n):
    total.append(int(input()))

total.sort()


answer=2,000,000,000

for i in range(n):
    for j in range(i+1,n,1):
        if(total[j]-total[i]>=m):
            if(total[j]-total[i]<answer):
                answer=total[j]-total[i]
            break

print(answer)
