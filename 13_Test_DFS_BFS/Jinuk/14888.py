from collections import deque

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

vals = []

q = deque()
q.append((a[0], (add, sub, mul, div), 0))
while q:
    now, op, count = q.popleft()
    if count == n-1:
        vals.append(now)
        continue
    if op[0] != 0:
        q.append((now + a[count+1], (op[0] - 1, op[1], op[2], op[3]), count + 1))
    if op[1] != 0:
        q.append((now - a[count+1], (op[0], op[1] - 1, op[2], op[3]), count + 1))
    if op[2] != 0:
        q.append((now * a[count+1], (op[0], op[1], op[2] - 1, op[3]), count + 1))
    if op[3] != 0:
        q.append((int(now / a[count+1]), (op[0], op[1], op[2], op[3] - 1), count + 1))

print(max(vals))
print(min(vals))