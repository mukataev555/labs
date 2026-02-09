n = int(input())
names = {}

for i in range(n):
    name = input().strip()
    if name  not in names:
        names[name] = 1

print(len(names))
