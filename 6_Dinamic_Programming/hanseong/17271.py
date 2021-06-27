
def fac(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

n, m= map(int,input().split())

k=n//m

result=1

for b in range(1,k+1):
    a=n-(b*m)
    if(a==0):
        result+=1
        break
    result+=(fac(a+b)// (fac(a) * fac(b)))
    
print(result%1000000007)
