INF = 1000000
a = [
[0,1,1,INF,INF,INF],
[1,0,INF,2,INF,INF],
[1,INF,0,INF,2,INF],
[INF,2,INF,0,INF,1],
[INF,INF,2,INF,0,1],
[INF,INF,INF,1,1,0],
]
for k in range(6):
    for i in range(6):
        for j in range(6):
            if (a[i][k] + a[k][j] < a[i][j]):
                a[i][j] = a[i][k]+a[k][j]
for l in a:
    print(l)