import bisect 
def solution(words, queries):
    # 각 10만 이하
    # 단어 길이 1만 이하 
    answer = []
    # 정방향부터 생각, 뒷 방향은 슬라이싱으로 해결시도. 
    words_lists = [[] for _ in range(10001)] 
    # 정렬하는데 걸리는 시간 ? 
    # word의 길이에 해당하는 idx에 단어 삽입
    for word in words: 
        words_lists[len(word)].append(word)
     
    for words in words_lists: 
        if words: 
            words.sort() 
    for query in queries: 
        words_idx = len(query)
        # fro??  
        if query[0] != '?': 
            start_idx = 0 
            end_idx = 0 
            for end_idx in range(1, words_idx): 
                if query[end_idx] == '?': 
                    break

            # 찾는 값이 있으면 -1 보다 큰 값 리턴
            # 찾는 값이 있으면 -1 보다 큰 값 리턴
            print(words_lists[words_idx], query[start_idx:end_idx], words_idx, start_idx, end_idx)
            left = binary_search_left(words_lists[words_idx], query[start_idx:end_idx], words_idx, start_idx, end_idx)
            right = binary_search_right(words_lists[words_idx], query[start_idx:end_idx], words_idx, start_idx, end_idx)
            print(left , right)
            if right >= 0 and left >= 0:
                print(right-left)
                answer.append(right-left)
           # 68 79 30  
                
        else: 
            pass 

    return answer
def binary_search_left(w_l, q, w_i, start_slice, end_slice):
    start = 0 
    end = w_i
    w_l_len = len(w_l)
    while start <= end: 
        mid = (start + end) // 2
        if (mid == 0 or q > w_l[mid - 1]) and w_l[mid] == q: 
        # if w_l[mid][start_slice:end_slice] == q and (mid == 0 or q > w_l[mid - 1]): 
            return mid 
        elif w_l[mid] >= q: 
            end = mid - 1
        else: 
            start = mid + 1

    return -1

def binary_search_right(w_l, q, w_i, start_slice, end_slice):
    start = 0 
    end = w_i
    w_l_len = len(w_l)
    while start <= end: 
        mid = (start + end) // 2
        # python 은 mid 0일때 w_l -1 검사해도 괜찮은 걸로 안다. -> -1이 맨뒤에있는 값을 찾기 때문이였다. 
        # if w_l[mid][start_slice:end_slice] == q and (mid == w_l_len-1 or q < w_l[mid+1]): 
        if (mid == w_l_len-1 or q < w_l[mid+1]) and w_l[mid][start_slice:end_slice]: 
            return mid 
        elif w_l[mid] > q: 
            end = mid - 1
        else: 
            start = mid + 1
    return -1

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
# 3 2 4 1 0p
