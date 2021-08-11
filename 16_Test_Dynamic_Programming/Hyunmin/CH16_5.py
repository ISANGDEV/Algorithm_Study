N = int(input())
dp = [0] * (N+1)  
ug_nums = [2, 3, 5]
dp[1] = 1  # 1은 못생긴 수

added_cnt = 0  # appended_count  
answer = []
i = 1  
while added_cnt < N:
    if added_cnt == 0: 
        answer.append(i)
        added_cnt += 1
        i += 1
        continue 
    for num in ug_nums: 
        if i % num == 0: 
            answer.append(i)
            added_cnt += 1 
            break 
    i += 1
print(added_cnt, i)
print(answer)
print(answer[added_cnt-1]) # + 1 


