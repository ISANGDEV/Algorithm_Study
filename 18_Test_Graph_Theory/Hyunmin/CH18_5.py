from collections import deque 
def topology_sort():
    result = [] 
    q = deque()  

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cycle_cnt = 0  # cycle  == 데이터에 일관성이 없어서 순위를 정할 수 없다 
    if len(q) >= 2:  # 진입차수 0인게 2개 이상이면 X  == 확실한 순위를 찾을 수 없다 
        return ["?"] 

    while q:
        cycle_cnt += 1 
        now = q.popleft()
        result.append(now)
        for k in range(1, n+1): 
            if graph[now][k]: 
                indegree[k] -= 1
                if indegree[k] == 0:
                    q.append(k)
    return result if cycle_cnt == n else ["IMPOSSIBLE"]


t = int(input())
answers = []
for _ in range(t): 
    n = int(input())
    teams = list(map(int, input().split()))  # 순위 팀 오름차순 
    m = int(input())
    changed = [list(map(int, input().split())) for _ in range(m)]
    
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n): 
        for j in range(i+1, n):
            graph[teams[i]][teams[j]] = True 
            indegree[teams[j]] += 1 
    
    for nums in changed: 
        a, b = nums[0], nums[1]
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True 
            indegree[a] += 1
            indegree[b] -= 1
        else: 
            # 
            graph[a][b] = True 
            graph[b][a] = False
            indegree[a] -= 1 
            indegree[b] += 1

    answers.append(topology_sort()) 

for answer in answers:
    for a in answer:
        print(a, end=" ")
    print()


