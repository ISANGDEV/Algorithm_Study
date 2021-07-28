from bisect import bisect_left
n=int(input())

house=list(map(int,input().split()))
house.sort()
result=(len(house)//2-1)
print(house[result])

