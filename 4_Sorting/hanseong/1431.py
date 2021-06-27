def comp(a):
    sum=0
    for i in a:
        if i<'A':
            sum+=int(i)
    return sum

def compare(i,j):

    if(len(guitar[i])>len(guitar[j])):
        guitar[i], guitar[j]=guitar[j], guitar[i]

    elif(len(guitar[i]) ==len(guitar[j])):
        a=comp(guitar[i])
        b=comp(guitar[j])

        if(a>b):
            guitar[i], guitar[j]=guitar[j], guitar[i]

        elif(a==b):
            if(guitar[i]>guitar[j]):
                guitar[i], guitar[j]=guitar[j], guitar[i]    

            

n= int(input())

guitar=[]

for i in range(n):
    a=list(input())     
    guitar.append(a)

for i in range(n):
    for j in range(i+1,n,1):
        compare(i,j)


for i in range(n):
    print(''.join(guitar[i]))
   

