def find_parent(parent, x): 
    if parent[x] != x: 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): 
    a = find_parent(parent, a) 
    b = find_parent(parent, b)
    if a < b: 
        parent[b] = a
    else:  
        parent[a] = b 


G = int(input())
P = int(input())
arr = [int(input()) for _ in range(P)]
parent = [0] * (G + 1)

for i in range(G+1): 
    parent[i] = i 

count = 0 
break_loop = False 
for p in arr: 
    for p_idx in range(p, 0, -1):  # 1까지만 반복해야됨 
        found_parent = find_parent(parent, p_idx) 

        if found_parent == 0: 
            break_loop = True 
        elif found_parent == p_idx: 
            union_parent(parent, p_idx-1, p_idx) 
            count += 1  
            break 
    if break_loop: 
        break 
print(count)
