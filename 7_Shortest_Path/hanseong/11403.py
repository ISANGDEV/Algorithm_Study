n = int(input())
visit = [0] *n
graph= []

def dfs(v):
    for i in range(n):
        if visit[i] == 0 and graph[v][i] == 1:
            visit[i] = 1
            dfs(i)

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    dfs(i)
    
    for j in range(n):
        if visit[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

    visit = [0] *n
