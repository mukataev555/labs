def valid(n):
    while n > 0:
        last_number = n % 10
        if last_number % 2 != 0:
            return False
        n = n // 10
    return True
        

n = int(input())
if valid(n):
    print ("Valid")
else:
    print("Not valid")






