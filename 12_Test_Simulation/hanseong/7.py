n=input()
half=len(n)/2
left=0
right=0

for i,num in enumerate(n):
    if(i<half):
        left+=int(num)
    else:
        right+=int(num)

if(left==right):
    print('LUCKY')
else:
    print('READY')

