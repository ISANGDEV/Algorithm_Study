def solution(N, stages):
    success = [0 for i in range(N+2)]
    fail = [0 for i in range(N+2)]
    
    for stage in stages:
        for i in range(1, stage+1):
            success[i] += 1
        fail[stage] += 1
        
    fail_rates = []
    
    for i in range(1, N+1):
        if success[i] == 0:
            rate = 0
        else:
            rate = fail[i] / success[i]
        fail_rates.append((i, -rate))
    
    fail_rates.sort(key = lambda x:x[1])
    result = []
    
    for fail_rate in fail_rates:
        result.append(fail_rate[0])
        
    return result
            