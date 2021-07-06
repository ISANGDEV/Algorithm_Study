n = int(input())

gongpo = list(map(int, input().split()))

gongpo.sort(reverse=True)

group = 0
idx = 0

while True:
    group += 1
    idx += gongpo[idx]
    if idx > len(gongpo):
        group -= 1
        break
    elif idx == len(gongpo):
        break
    
print(group)