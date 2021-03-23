n, m, k= map(int, input().split())

data=list(map(int, input().split()))

data.sort()
result=0
print(data)
if(data[n-1]==data[n-2]):
    result=data[n-1]*m
else:
    result=((data[n-1]*k)+data[n-2])*(m//(k+1))+ data[n-1]*(m%(k+1))

print(result)
