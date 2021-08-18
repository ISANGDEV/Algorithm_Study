N,M=map(int,input().split())
INF=10**6
adj = [[INF]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    adj[a][b]=1
for i in range(1,N+1):
    for j in range(1,N+1):
        adj[i][j]=0
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            adj[a][b]=min(adj[a][b],adj[a][k]+adj[k][b])
result=0
for i in range(1,N+1):
    cnt=0
    for j in range(1,N+1):
        if(adj[i][j]!=INF or adj[j][i]!=INF):
            cnt+=1
    if(cnt==N):
        result+=1
print(result)