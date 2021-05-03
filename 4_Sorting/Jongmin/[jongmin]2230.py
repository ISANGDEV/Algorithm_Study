N,M=map(int,input().split())
result=[]
for i in range(N):
    result.append(int(input()))
result.sort()
left=0
right=0
diff= result[len(result)-1]-result[0]
cur=0
while(left<=right and right<len(result)):
    cur = result[right] - result[left]
    if(M<=cur<diff):
        diff = cur
    if(cur<M):
        right+=1
    elif(cur==M):
        diff=cur
        break
    else:
        left+=1
print(diff)
