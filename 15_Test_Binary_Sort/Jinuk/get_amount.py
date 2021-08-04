n, x = map(int, input().split())
numbers = list(map(int, input().split()))

def first(numbers, target):
    left, right = 0, n-1
    while True:
        if left > right:
            return -1
        mid = (left+right) // 2
        if (mid == 0 or numbers[mid-1] < target) and numbers[mid] == target:
            return mid
        elif numbers[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    

def last(numbers, target):
    left, right = 0, n-1
    while True:
        if left > right:
            return -1
        mid = (left+right) // 2
        if (mid == n-1 or numbers[mid+1] > target) and numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
def count(numbers, target):
    fi = first(numbers, target)
    if fi == -1:
        return -1

    la = last(numbers, target)

    return la - fi + 1

print(count(numbers, x))
