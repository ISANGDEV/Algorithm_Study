DIV=10**9+7
powdict={0:1,1:2}
def popow(a):
    global powdict
    if a in powdict:
        return powdict[a]
    else:
        if(a%2==0):
            result=popow(a//2)**2
            powdict[a]=result%DIV
            return result
        else:
            result=popow(a//2)**2
            result*=2
            powdict[a]=result%DIV
            return result

N=int(input())
result=0
for i in range(N):
    C,K=map(int, input().split())
    result+=C*K*popow(K-1)
print(result%DIV)