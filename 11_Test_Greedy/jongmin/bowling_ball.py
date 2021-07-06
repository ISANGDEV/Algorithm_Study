N,M=map(int, input().split())
weightMap={i:0 for i in range(1,11)}
balls=input().split()
for i in balls:
    weightMap[int(i)]+=1
result=0
tempsum=0
for key in weightMap:
    tempsum+=weightMap[key]
    result+=weightMap[key]*(N-tempsum)
print(result)