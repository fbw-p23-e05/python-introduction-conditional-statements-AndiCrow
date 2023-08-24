# #Task1
num1 = int(input("give me a number"))
num2 = int(input("give me a number"))
num3 = int(input("give me a number"))

sum_num = num1 + num2 + num3
if num1 == num2 == num3:
    print("First", num1 )
    print("Second", num2)
    print("Third", num3)
    print("The triple sum is:",sum_num * 3)
else:
    print("First", num1 )
    print("Second", num2)
    print("Third", num3)
    print("The sum is:",sum_num)

# #Task2

num1 = int(input("give me a number"))
num2 = int(input("give me a number"))

diff_num = num1 - num2

if num1 > num2:
    print("First", num1 )
    print("Second", num2)
    print("The result of calculation is", diff_num * 2)
else:
    print("First", num1 )
    print("Second", num2)
    print("The result of calculation is", abs(diff_num))

# #Task3

num = int(input("give me a number"))

if num % 2== 0:
    print("Number to check:", num)
    print(num, "is an even nummber!")
else:
    print("Number to check:", num)
    print(num, "is an odd nummber!")


# #Task4

import math

radius = float(input("Input the radius of the circle : "))
round_radius = round(radius, 2)
area = math.pi * round_radius**2 

print("the radius of the circle :", round_radius)
print("The area of the circle with radius", round_radius, "is:", area)

# #Task 5

guess = int(input("Put your guess number between 1 to 10 here: "))
correct_num = 8
while True:
    if guess == correct_num:
        print("Well guessed!")
        break
    else:
        print("Guess a number between 1 and 10 until you get it right:", guess)
        guess = int(input("Put your guess number between 1 to 10 here: "))

# #Task 6

temp = float(input("Enter the temperature"))
scal = input("Enter the scale (C for Celsius, F for Fahrenheit): ")

Fahrenheit_to_Cels = (temp -32) % 5 * 9
Cels_to_Fahrenheit = temp * 9  % 5 + 32 

if scal == "C":
    Fahrenheit_temp = Cels_to_Fahrenheit
    print("Equivalent Fahrenheit temperature:", Fahrenheit_temp, "°F")
elif scal == "F":
    Cels_temp = Fahrenheit_to_Cels
    print("Equivalent Celsius temperature:", Cels_temp, "°C")


#Task 7
rows = 5
for i in range(1, rows+ 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(rows -1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#Task 8


num1 = 0
num2 = 1
next_num = num2
count = 1

print(num1, end=" ")
print(num2, end=" ")

while num1 <= 50:
    if num1 >=-1:
        print(next_num, end=" ")
    count += 1
    num1, num2 = num2, next_num
    next_num = num1 + num2
print()