import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    name, korean, english, math = input().split()
    students.append((name, korean, english, math))

students.sort()
students.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
