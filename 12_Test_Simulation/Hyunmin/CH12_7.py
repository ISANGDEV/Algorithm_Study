import itertools
n, m = map(int, input().rstrip().split())

map_arr = []
for _ in range(n):
    map_arr.append(list(map(int, input().rstrip().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if map_arr[i][j] == 1:
            home.append([i+1, j+1])
        elif map_arr[i][j] == 2:
            chicken.append([i+1, j+1])  
        
best = mid = h_shortest = 1e9  # 100이면 충분할것이라고 생각했으나 아님. 1e9를 사용하자 
for i in range(m):
    result = list(itertools.combinations(chicken, i+1))
    for c in result:
        mid = 0
        # 다 더하는데, c의 요소가 여러개일 때((2, 3) or( 4, 5))는 요소들중에서 작은 값을 찾아서 더해야함
        for h in home:
            h_shortest = 1e9
            for sc in c:
                path = abs(h[0] - sc[0]) + abs(h[1] - sc[1])
                if path < h_shortest:
                    h_shortest = path
            mid += h_shortest
        if mid < best:
            best = mid
print(best)

# 0 1 2 3 4
# doing
# total1 = total2 = total3 = 1000
#
# for i in range(m):
#     for j in range(len(chicken)):
#         total3 = 0
#         for h in home:
#             min_length = 1000
#             for c in chicken[j:len(chicken):i+1]:
#                 path = abs(h[0] - c[0]) + abs(h[1] - c[1])
#                 if path < min_length:
#                     min_length = path
#             total3 += min_length
#         if total3 < total2:
#             total2 = total3
#     if total2 < total1:
#         total1 = total2
# print(total1)



# for h in home:
#     temp = []
#     max_length = 1000
#     for c in chicken:
#         path = abs(h[0]-c[0]) + abs(h[1]-c[1])
#         if path < max_length:
#             max_length = path
#             temp = c
#     temp[2] += 1
# chicken.sort(key=lambda x: -x[2])
#
#
# for i in range(len(chicken)):
#     if chicken[i][2] > 0 and i < m:
#         continue
#     else:
#         m = i
#         break
#
# total_length = 0
# for h in home:
#     max_length = 1000
#     for c in range(m):
#         path = abs(h[0]-chicken[c][0]) + abs(h[1]-chicken[c][1])
#         if path < max_length:
#             max_length = path
#     total_length += max_length
#
#
#







