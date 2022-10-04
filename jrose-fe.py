import math
print("Enter the first coordinates:" )
x1 , y1 = (input().split())
print("Enter the second coordinates:" )
x2 , y2 = (input().split())
dist = math.sqrt(((x2-x1)**2) + (y2-y1)**2)
print(dist)
