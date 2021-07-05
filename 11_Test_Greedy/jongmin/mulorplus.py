S=list(map(int, list(input())))
result=S[0]
for i in range(1,len(S)):
    r=S[i]
    if(r!=0 and r!=1 and result!=0 and result!=1):
        result*=r
    else:
        result+=r
print(result)