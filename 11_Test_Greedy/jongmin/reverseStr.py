S=list(map(int, list(input())))
cnt=[0,0]
cnt[S[0]]=1
for i in range(len(S)-1):
    if(S[i]!=S[i+1]):
        cnt[S[i]]+=1
print(min(cnt))
