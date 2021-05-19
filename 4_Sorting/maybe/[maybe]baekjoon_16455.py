def kth(a, k):
    n = len(a)

    count = [0]*(n+1)
    countSum = [0]*(n+1)

    for i in range(0, n):
        count[a[i]] += 1

    countSum[0] = count[0]
    for i in range(1, n+1):
        countSum[i] = countSum[i-1]+count[i]

    b = [0]*(n+1)
    for i in range(n-1, -1, -1):
        b[countSum[a[i]]] = a[i]
        countSum[a[i]] -= 1

    ans = b[k]

    return ans
