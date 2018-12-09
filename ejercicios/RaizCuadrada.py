import math

print("introduce el numero de inicio del sumatorio")
a = input()
print("introduce el numero de fin del sumatorio")
b = input()

if 0 <= a <= b:
    result = 0
    while a <= b:
        result += math.sqrt(a)
        a += 1
    print result