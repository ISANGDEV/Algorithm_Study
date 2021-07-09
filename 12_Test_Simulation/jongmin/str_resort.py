S=input()
sum=0
digit='0123456789'
stringbuf=[]
for token in S:
    if token in digit:
        sum+=int(token)
    else:
        stringbuf.append(token)
stringbuf.sort()
print(''.join(stringbuf)+str(sum))