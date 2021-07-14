s=list(input())
s.sort()
a=''
for i in range(len(s)):
    if(ord(s[i])>57):
        a+="".join(s[i:])+"".join(s[:(i-1)])
        break
print(a)
