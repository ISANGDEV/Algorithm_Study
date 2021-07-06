N=int(input())
st=[]
for i in range(N):
    st.append(float(input()))
st.sort()
for i in range(7):
    print(format(st[i],".3f"))