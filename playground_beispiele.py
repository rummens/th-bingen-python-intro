def moveForward():
    pass

moveForward()

for i in range(1, 5):
    print(i)

a = 2
b = 10

if a > 3:
    print("a ist größer als 3")
elif a < 3:
    print("a ist kleiner als 3")
elif a == 3 and b == 10:
    print("a ist gleich 3 und b ist gleich 10")
elif a == 3 or b == 3:
    print("a ist gleich 3 oder b ist gleich 3")
else:
    print("a ist gleich 3")

def add_two_numbers(number1, number2):
    return number1 + number2

added_number = add_two_numbers(a, b)
print(added_number)