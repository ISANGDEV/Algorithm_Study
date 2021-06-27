from collections import deque
N=int(input())
time=[0]*(N+1)
graph=[[] for i in range(N+1)]
indegree=[0]*(N+1)
addTime=[0]*(N+1)
def topology_sort():
    result=[i for i in time]
    q=deque()
    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in range(1,N+1):
        print(result[i])


for i in range(N):
    cmdInput=list(map(int, input().split()))
    time[i+1]=cmdInput[0]
    precedeLectureNums=cmdInput[1:-1]
    for lectureNum in precedeLectureNums:
        graph[lectureNum].append(i+1)
        indegree[i+1]+=1
topology_sort()