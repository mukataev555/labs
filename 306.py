class Rectangle:
    width, length = map(int, input().split())
    area = lambda width, length : width * length
    print(area(width,length)) 

p1 = Rectangle()
p1
