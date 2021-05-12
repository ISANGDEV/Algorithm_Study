n, h=map(int, input().split())

d_obs=(h+1)*[0]
u_obs=(h+1)*[0]


for i in range(n):
    a=int(input())
    if(i%2==0):
            d_obs[a]+=1
    else:
            u_obs[a]+=1





for i in range(h-1,0,-1):
        d_obs[i]+=d_obs[i+1]
        
        u_obs[i] += u_obs[i+1]





u_obs.reverse()

total=[0] * h
for i in range(h):
    total[i]=d_obs[i+1]+u_obs[i]


b=min(total)

print(b, total.count(b))
