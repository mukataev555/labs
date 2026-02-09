n = int(input())
a  = list(map(int, input().split()))

for i in a:
    a.sort(reverse = True)

for i in a:
    print (i, end = " ")