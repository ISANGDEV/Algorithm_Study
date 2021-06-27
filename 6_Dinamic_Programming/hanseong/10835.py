n=int(input())

left=list(map(int,input().split()))
right=list(map(int,input().split()))
result=[[0 for _ in range(n+1)] for _ in range(n+1)]
i=0
j=0


    
def search(left, right):

    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if(left[j]>right[i]):
                result[i][j]=result[i+1][j]+right[i]
            else:
                result[i][j]=max(result[i+1][j+1],result[i][j+1])
                

    return result[0][0]

ans=0
ans=search(left,right)
print(ans)

