n = int(input())
names = {}

for i in range(n):
    name = input().strip()
    if name not in names:
        names[name] = 1
    else:
        names[name] += 1

count = 0
for x in names:
    if names[x] == 3:
        count += 1

print(count)
