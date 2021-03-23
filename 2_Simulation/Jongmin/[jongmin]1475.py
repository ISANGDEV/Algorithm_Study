import math
N=list(input())
counts=[0]*10
for i in N:
    if(i!='6' and i!='9'):
        counts[int(i)]+=1
print(max(max(counts),math.ceil((N.count('6')+N.count('9'))/2)))
