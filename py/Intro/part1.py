from math import sqrt
''''
name = input("what's your name?")
print("Hi, there " + name)

print("!" + name + "!" + name + "!")
print("----------")

name1 = input("What is your name?")


name2 = input("What is your family name ? ")


adress1 = input("What is street address?")


adress2 = input("What is your city and postal code?")
'''''

'''''
print(name1+" "+name2)
print(adress1)
print(adress2)
print("----------")
'''''
'''''
part = input("The 1st part: ")
part1 = input("The 2nd part: ")
part2 = input("The 3rd part: ")
print(part+ "-"+part1+"-"+part2+"!")
print("----------")
'''''
'''''
name = input("Please type in a name:")
year = input("Please type in a year: ")

print(name+" is a valiant knight, born in the year "+year+". One morning "+name+" woke up to an awful racket: a dragon was approaching the village. Only "+name+" could save the"
                                                                                                                                                                " village's residents.")
print("----------")
'''''
'''''
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")

print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")

print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")
print("----------")
'''''
'''''
x = 27
y = 15

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")
print("----------")
'''''
'''''
print(5 , end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)
print("----------")
'''''
'''''
number = int(input("Please type un a number :"))
print(f"{number} times 5 is {number * 5}")
print("----------")
'''''
'''''
name = str(input("What is your name?"))
year = int(input("Which year were you born?"))
print(f"Hi {name},you will be {2021-year} years old at the end of the year 2021")
print("----------")
'''''
'''''
days = int(input("How many days? "))
Seconds = int(86400)
print(f"Seconds in that many days:{days * Seconds}")
print("----------")
'''''
'''''
number1= int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
print(f"The product is {number1 * number2 * number3}")
print("----------")
'''''
'''''
sum = 0
product = 0


number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

sum = number1+number2
product = number1*number2


print(f"The sum of the numbers: {sum} ")
print(f"The product of the numbers: {product} ")
print("----------")
'''''
'''''
sum = 0
mean = 0

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))

sum = number1+number2+number3+number4
mean = sum/4

print(f"The sum of the numbers is {sum} and the mean is {mean}")
print("----------")
'''''
'''''
times = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("he price of a typical student lunch?"))
money = float(input("How much money do you spend on groceries in a week? "))

weekly = (times*price)+money
daily = weekly/7


print("Average food expenditure:")
print(f"Daily: {daily} euros ")
print(f"Weekly: {weekly} euros")
print("----------")
'''''

'''''
students_number = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
answer = students_number//group_size
if students_number%group_size == 0 :
    answer+=0
else:
    answer +=1
print(f"Number of groups formed: {answer}")
print("----------")
'''''
'''''
number = int(input("Please type in a number: "))
if(number==1984) :
    print("Orwell")

print("----------")
'''''
'''''
number = int(input("Please type in a number: "))
if(number<0):
    print(f"The absolute value of this number is {number * (-1)}")
else:
    print(f"The absolute value of this number is {number}")

print("----------")
'''''
'''''
name = str(input("Please tell me your name: "))
cost = float(5.90)
if (name=="Jerry"):
    print("Next please!")
else:
    portion = int(input("How many portions of soup? "))
    print(f"The total cost is {cost * portion}")
    print("Next please!")
print("----------")
'''''
'''''
number = int(input("Please type in a number: "))
if(number>1000):
    print("")
if(number<10):
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
if(number>10):
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
if(number>100):
    print("This number is smaller than 1000")

print("Thank you!")
print("----------")
'''''
'''''
number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
operation = str(input("Operation: "))
if operation=="add":
    print(f"{number_one} + {number_two} = {number_one + number_two}")
if operation=="subtract":
    print(f"{number_one} - {number_two} = {number_one - number_two}")
if operation=="multiply":
     print(f"{number_one} * {number_two} = {number_one * number_two}")
else:
    print()
print("----------")
'''''
'''''
temp_F = int(input("Please type in a temperature (F): "))
temp_C = (temp_F-32)* 5/9
if(temp_C<0):
    print(f"{temp_F} degrees Fahrenheit equals {temp_C} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{temp_F} degrees Fahrenheit equals {temp_C} degrees Celsius")
print("----------")
'''''
'''''
H_wa = float(input("Hourly wage:"))
H_wo = int(input("Hours worked:"))
day_week = str(input("Day of the week:"))

if(day_week=="Sunday"):
    print(f"Daily wages: {(H_wa*2)*H_wo} euros")
else:
    print(f"Daily wages: {H_wa*H_wo} euros")
print("----------")
'''''
'''''
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

else:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")
print("----------")
'''''
'''''
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ").lower() == "yes"

outfit = "Wear jeans and a T-shirt"

if temp > 20:
    pass  # no need to suggest additional clothing
elif temp > 10:
    outfit += "\nI recommend a jumper as well"
elif temp > 5:
    outfit += "\nI recommend a jumper as well\nTake a jacket with you"
else:
    outfit += "\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order"

if rain:
    outfit += "\nDon't forget your umbrella!"

print(outfit)
print("----------")
'''''
'''''
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
x1 = (-b+sqrt((b**2)-4*a*c))/(2*a)
x2 = (-b-sqrt((b**2)-4*a*c))/(2*a)
print(f"The roots are {x1} and {x2}")
print("----------")
'''''
