N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
aidx=0
for i in range(K):
    if(A[aidx]<B[i]):
        A[aidx]=B[i]
        aidx+=1
    else:
        break
print(sum(A))