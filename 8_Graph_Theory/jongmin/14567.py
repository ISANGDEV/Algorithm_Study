from collections import deque
N,M=map(int, input().split())
graph=[[] for i in range(N+1)]
semesters=[1]*(N+1)
indegree=[0]*(N+1)

for i in range(M):
    precedeSubject, followingSubject=map(int, input().split())
    indegree[followingSubject]+=1
    graph[precedeSubject].append(followingSubject)

q=deque()
for i in range(1,N+1):
    if(indegree[i]==0):
        q.append(i)
while q:
    subjectNum=q.popleft()
    for followingSubject in graph[subjectNum]:
        semesters[followingSubject]=max(semesters[followingSubject],1+semesters[subjectNum])
        indegree[followingSubject]-=1
        if(indegree[followingSubject]==0):
            q.append(followingSubject)
for i in range(1,N+1):
    print(semesters[i],end=' ')