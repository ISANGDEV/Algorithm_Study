n=int(input())

dic=[]
temp=[]
for i in range(n):
    a,b,c,d=input().split()
    temp=[a,int(b),int(c),int(d)]
    dic.append(temp)

dic=sorted(dic,key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(len(dic)):
    print(dic[i][0])
