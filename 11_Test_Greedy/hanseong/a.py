t=int(input())
for _ in range(t):
    a=input()
    result=[]
    for i,k in enumerate(a):
        k=int(k)
        if (i%2==0):
           
            k*=2
            if(k>=10):
                k-=9
           
        result.append(k)
    if(sum(result)%10==0):
        print('T')
    else:
        print('F')
            
            
                
        
