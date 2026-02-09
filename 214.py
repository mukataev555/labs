n = int(input())
arr = list(map(int, input().split()))

s = {}

for x in arr:
    if x in s:
        s[x] += 1
    else:
        s[x] = 1

max_count = 0
answer = 0

for x in s:
    if s[x] > max_count:
        max_count = s[x]
        answer = x
    elif s[x] == max_count and x < answer:
        answer = x

print(answer)
