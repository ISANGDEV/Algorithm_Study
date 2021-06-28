from collections import deque
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    buildingAmount,ruleAmount=map(int, sys.stdin.readline().split())
    buildingTimes=list(map(int, sys.stdin.readline().split()))
    buildingTimes=[0]+buildingTimes
    basisTimes=[i for i in buildingTimes]
    graph=[[] for i in range(buildingAmount+1)]
    indegree=[0]*(buildingAmount+1)
    for i in range(ruleAmount):
        precedingBuilding,followingBuilding=map(int, sys.stdin.readline().split())
        graph[precedingBuilding].append(followingBuilding)
        indegree[followingBuilding]+=1
    winningBuildingNumber=int(sys.stdin.readline())
    q=deque()
    for i in range(1,buildingAmount+1):
        if(indegree[i]==0):
            q.append(i)
    while q:
        precedingBuilding=q.popleft()
        for followingBuilding in graph[precedingBuilding]:
            buildingTimes[followingBuilding]=max(buildingTimes[followingBuilding],basisTimes[followingBuilding]+buildingTimes[precedingBuilding])
            indegree[followingBuilding]-=1
            if(indegree[followingBuilding]==0):
                q.append(followingBuilding)
    print(buildingTimes[winningBuildingNumber])
