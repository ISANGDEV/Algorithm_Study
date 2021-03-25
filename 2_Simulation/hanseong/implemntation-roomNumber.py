import math
n=list(map(int, input()))
total=[]
count=0

for i in range(10):
    total.append(n.count(i))
count=max(math.ceil((total[6]+total[9])/2),max(total[0:6]),max(total[7:9]))
print(count)
            
        
