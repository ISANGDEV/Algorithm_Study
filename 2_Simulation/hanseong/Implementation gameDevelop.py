n, m= map(int, input().split())

a, b, d= map(int, input().split())

total=[]
count=1
na,nb=0,0



for i in range(n):
    total.append(list(map(int,input().split())))

 
while True:
    d-=1
    if(d==-1):
        d=3
    if(d==3 and a>1 and total[a-1][b]==0):
        a-=1
        count+=1
        total[a][b]=1
    elif(d==2 and b<m and total[a][b+1]==0):
        b+=1
        count+=1
        total[a][b]=1
    elif(d==1 and a<m and total[a+1][b]==0):
        a+=1
        count+=1
        total[a][b]=1
    elif(d==0 and b>1 and total[a][b-1]==0):
        b-=1
        count+=1
        total[a][b]=1
    elif((total[a][b-1]==1 or b==1) and (total[a][b+1]==1 or b+1==m)and (total[a-1][b]==1 or a==1)and (total[a+1][b]==1 or a+1==n)):
        if(d==0 and total[a][b+1]==0):
            b+=1
            count+=1
            total[a][b]=1
        elif(d==1 and total[a-1][0]==0):
            a-=1
            count+=1
            total[a][b]=1
        elif(d==2 and total[a][b-1]):
            b-=1
            count+=1
            total[a][b]=1
        elif(d==3 and total[a+1][b]):
            a+=1
            count+=1
            total[a][b]=1
        else:
            break

print(count)
    
        
            
