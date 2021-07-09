N=input()
print('LUCKY' if sum(list(map(int, N[:len(N)//2])))==sum(list(map(int, N[len(N)//2:]))) else 'READY')