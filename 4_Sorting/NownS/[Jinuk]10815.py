n = int(input())
have = list(map(int, input().split()))
m = int(input())
question = list(map(int, input().split()))

have.sort()

def binary_search_index(sorted_arr, val, left, right):
    if left>right:
        return False
    point = (left+right)//2
    if sorted_arr[point] > val:
        return binary_search_index(sorted_arr, val, left, point-1)
    elif sorted_arr[point] < val:
        return binary_search_index(sorted_arr, val, point+1, right)
    elif sorted_arr[point] == val:
        return True
    else:
        return False

for num in question:
    if binary_search_index(have, num, 0, len(have)-1):
        print(1, end=" ")
    else:
        print(0, end=" ")