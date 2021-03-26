import sys
N=int(input())
numbers=[0]*8001
maximum=-4001
minimum=4001
sumation=0
length=0
many=[]
maxcount=0
for i in range(N):
    num=int(sys.stdin.readline().rstrip())
    sumation+=num
    #범위위해 최대 최소값
    maximum=max(maximum,num)
    minimum=min(minimum,num)
    #배열에 개수 카운팅(중앙값)
    numbers[num+4000]+=1
    length+=1
    #최빈값
    if(maxcount<numbers[num+4000]):
        maxcount=numbers[num+4000]
        many=[num]
    elif(maxcount==numbers[num+4000]):
        many.append(num)
print(int(round(sumation/N,0)))
middle=N//2
idx=0
result=-1
#중앙값찾기
for i in range(minimum+4000,maximum+4001):
    idx+=numbers[i]
    if(idx>=middle+1):
        result=i-4000
        break
print(result)
many.sort()
if(len(many)==1):
    print(many[0])
else:
    print(many[1])
print(maximum-minimum)
