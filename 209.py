n = int(input())
a = list(map(int, input().split()))

max = a[0]
min = a[0]

for i in a:
    if i > max:
        max = i

for i in a:
    if i < min:
        min = i
    
for i in a:
    if i == max:
        i = min
    print(i, end = " ")


