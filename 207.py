n=int(input())
number=list(map(int, input().split()))
max = number[0]
index = 0
i = 0
for x in number:
    if x > max:
        max = x
        index = i
    i += 1
print (index + 1)
