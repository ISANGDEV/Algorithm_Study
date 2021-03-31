import collections

n=int(input())

total=[0]*n

for i in range(n):
    total[i]=int(input())
total.sort()

sum=0

for i in total:
    sum+=i
print(round(sum/n))

print(total[n//2])

total_dict=collections.Counter(total)

most_list=total_dict.most_common()

max_num=most_list[0][1]

most=[]
for i,j in most_list:
    if(j==max_num):
        most.append(i)

most.sort()

if(len(most)>1):    
    print(most[1])
else:
    print(most[0])


print(total[len(total)-1]-total[0])

