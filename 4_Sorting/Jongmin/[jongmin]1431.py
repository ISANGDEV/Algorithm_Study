import functools
N=int(input())
def compare(x,y):
    if(len(x)!=len(y)):
        return len(x)-len(y)
    else:
        countx=0
        county=0
        for token in x:
            if(token.isdigit()):
                countx+=int(token)
        for token in y:
            if (token.isdigit()):
                county += int(token)
        if(countx!=county):
            return countx-county
        else:
            if(x<y):
                return -1
            else:
                return 1
result=[]
for i in range(N):
    result.append(input())
result.sort(key=functools.cmp_to_key(compare))
for r in result:
    print(r)