n = int(input())
a = list(map(int, input().split()))

m = [] 
for i in a:
    if i in m:
        print("NO")
    else:
        print("YES")
        m.append(i)