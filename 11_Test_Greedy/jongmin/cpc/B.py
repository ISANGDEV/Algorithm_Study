N=int(input())
histogram=[]
for i in range(N):
    histogram.append(int(input()))
histogram.sort()
S=histogram[0]*N
i=1
while S<=histogram[i]*(N-i):
    i+=1
    S=histogram[i]*(N-i)
print(S)