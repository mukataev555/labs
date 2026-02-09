n = int(input())
count = 0
x = 0
while (n >= 2 ** x):
    if n == 2**x:
        count +=1
        break
    x +=1
if (count > 0):
    print ("YES")
else:
    print ("NO")


