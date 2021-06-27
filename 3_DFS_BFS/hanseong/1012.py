t=int(input())

def search(graph, i, j):
    graph[i][j]=0
    
    if(j<m-1 and graph[i][j+1]==1):
        search(graph, i, j+1)
         
    if(i<n-1 and graph[i+1][j]==1):
        search(graph, i+1, j)

    
for i in range(t):
    m, n, k= map(int, input().split())

    count=0

    graph=[[0]*m for _ in range(n)]

   
    for i in range(k):
        x, y=map(int, input().split())
        
        graph[y][x]=1
        
        
    for i in range(n):
         for j in range(m):
           if(graph[i][j]==1):
               count+=1
               search(graph, i, j)
         
    
    print(count)
      


