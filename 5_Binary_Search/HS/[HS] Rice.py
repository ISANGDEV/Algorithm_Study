def partition(list,st,ed):
    pivot = list[st]
    left = st + 1
    right = ed
    while 1 :
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] > pivot:
            right -= 1

        if right < left :
            break

        else:
            list[left], list[right] = list[right],list[left]
    list[st],list[right] = list[right],list[st]

    return right # 새로운 pivot 값

def kth(a,k):
    stack = [[0,len(a)-1]]
    l = a

    while stack:
        left,right = stack.pop()
        pivot = partition(l,left,right)

        if pivot+1 == k:
            return a[pivot]
        elif pivot +1 < k:
            stack.append([pivot+1,right])
        else:
            stack.append([left,pivot-1])
