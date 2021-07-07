n=int(input())
result=[]
min_ix=10000000
for i in range(n):
    a=int(input())
    if(i==0):
        result.append(a)
    
    elif(min_ix>a):
        a,min_ix=min_ix,a
        if((min_ix*(i+1))>result[-1]):
            result.append(min_ix*(i+1))
        else:
            result.append(result[-1])
    else:result.append(min_ix*(i+1))
    print(result)
print(result[-1])
