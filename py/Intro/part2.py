from math import sqrt
'''''
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number-100}")
    print(f"{number-100} must be my lucky number!")
    print("Have a nice day!")

else:
   print(f"{number} must be my lucky number!")
   print("Have a nice day!")

'''''


'''''
word = str(input("Please type in a word:"))
length = len(word)
if length <= 1:
    print()
else:
    print(f"There are {length} in the word {word}")

print("Thank you!")
'''''

'''''
number = float(input("Please type in a temperature: "))
integer = int(number)
decimal = number - integer
print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")
'''''

'''''
age = int(input("How old are you?"))
if age>=18:
    print("You are of age!")
else:
    print("You are not of age!")
'''''
'''''
number = int(input("Please type in the first number: "))
other_number = int(input("Please type in another number: "))
if number>other_number:
    print(f"The greater number was:{number}")
elif other_number>number:
    print(f"The greater number was:{other_number}")
else:
    print("The numbers are equal!")
'''''

'''''
print("Person 1:")
name_person1 = str(input("Name:"))
age_person1 = int(input("Age:"))

print("Person 2:")
name_person2 = str(input("Name:"))
age_person2 = int(input("Age:"))

if age_person1>age_person2:
    print(f"The elder is {name_person1}")
elif age_person2>age_person1:
    print(f"The elder is {name_person2}")
else:
    print(f"{name_person1} and {name_person2} are the same age")
'''''

'''''
firstword = (input("Please type in the 1st word:")).lower()
secondword = (input("Please type in the 2nd word:")).lower()

if firstword<secondword:
    print(f"{secondword} comes alphabetically last")
elif firstword>secondword:
    print(f"{firstword} comes alphabetically last")
else:
    print("You gave the same word twice.")
'''''

'''''
age = int(input("What is your age?"))
if age < 5 and age > 0:
    print("I suspect you can't write quite yet...")
    print("That must be a mistake")

elif age <= 0:
    print("That must be a mistake")

else:
    print(f"Ok, you're {age} years old")
'''''
'''''
name = input("Please type in your name: ")

if name in ["Huey", "Dewey", "Louie"]:
    print("I think you might be one of Donald Duck's nephews.")
elif name in ["Morty", "Ferdie"]:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")
'''''

'''''
note = int(input("How many points [0-100]:"))
if note < 0:
    print("Grade: impossible!")
elif note >= 0 and note <= 49:
    print("Grade: fail")
elif note >= 50 and note <= 59:
   print("Grade: 1")
elif note >= 60 and note <= 69:
    print("Grade: 2")
elif note >= 70 and note <= 79:
    print("Grade: 3")
elif note >= 80 and note <= 89:
    print("Grade: 4")
elif note >= 90 and note <=100:
    print("Grade: 5")
else:
    print("Grade: impossible!")
'''''

'''''
#FizzBuzz
number = int(input("Number:"))
if number % 3 == 0 and not(number % 5 ==0):
    print("Fizz")
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0 and not(number % 3 == 0):
    print("Buzz")
else:
    print("")
'''''
'''''
#Leap Year
year = int(input("Please type in a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
'''''
'''''
#alphabetic in the middle
first_letter = input("1st letter:")
second_letter = input("2nd letter:")
third_letter = input("3rd letter: ")
middle = ""
if first_letter < second_letter:
    if first_letter > third_letter:
        middle = first_letter
    elif second_letter < third_letter:
        middle = second_letter
    else:
        middle = third_letter
else:
    if first_letter < third_letter:
        middle = first_letter
    elif second_letter > third_letter:
        middle = second_letter
    else:
        middle = third_letter

print(f"The letter in the middle is {middle}")
'''''
'''''
#Finnish Gift tax calculator
gift = int(input("Value of gift: "))

if gift < 5000:
    print("No tax!")
else:
    if gift >= 5000 and gift < 25000:
        tax = (100 + (gift - 5000) * 0.08)
        print(f"Amount of tax: {tax} euros")
    elif gift >= 25000 and gift < 55000:
        tax = (1700 + (gift - 25000) * 0.10)
        print(f"Amount of tax: {tax} euros")
    elif gift >= 55000 and gift < 200000:
        tax = (4700 + (gift - 55000) * 0.12)
        print(f"Amount of tax: {tax} euros")
    elif gift >= 200000 and gift < 1000000:
        tax = (22100 + (gift - 200000) * 0.15)
        print(f"Amount of tax: {tax} euros")
    elif gift >= 1000000:
        tax = (142100 + (gift - 1000000) * 0.17)
        print(f"Amount of tax: {tax} euros")
'''''
'''''
#Loop While 1
while True:
    print("hi")
    msg = input("Shall we continue?")
    if msg == "no":
        break
print("okay then")
'''''
'''''
#Loop While 2
while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        print("Exiting...")
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))
'''''
'''''
#Loop while 3 Countdown
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number == 0:
    break

print("Now!")
'''''
'''''
#Loop while 4 repeat password
password = input("Password:")
while True:
    msg = input("Repeat password:")
    if password==msg:
        break
    else:
        print("They do not match!")

print("User account created!")
'''''
'''''
#Loop while 5 PIN and number of attempts
attempt = 0

while True:
    code = input("PIN:")
    attempt += 1
    if code == "4321":
        if attempt == 1:
            print(f"Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempt} attempts")
        break
    else:
        print("Wrong")
'''''
'''''Dans ce code, la variable next_leapyear est initialisée au prochain multiple de 4 supérieur
 ou égal à l'année saisie. ' Ensuite, la boucle continue d'ajouter 4 années à next_leapyear jusqu'à ce qu'une année
  bissextile soit atteinte.
L'année bissextile suivante correcte est alors imprimée et la boucle se termine par l'instruction break.
'''''
'''''
#Loop while 6 : Next leap year
year = int(input("Year: "))
next_leapyear = year + 4 - (year % 4)
while True:
    if next_leapyear % 4 == 0 and (next_leapyear % 100 != 0 or next_leapyear % 400 == 0):
        print(f"The next leap year after {year} is {next_leapyear}")
        break
    else:
        next_leapyear += 4
'''''
'''''
#Loop while 7
story = ""
previous_word = None
while True:
    word = input("Please type in a word:")
    if word=="end" or word==previous_word:
        print(story)
        break
    story += word + " "
    previous_word = word
'''''
'''''
print("Please type in integer numbers. Type in 0 to finish.")
all = 0
sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    elif number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    all += 1
    sum += number

if all == 0:
    mean = 0
else:
    mean = sum / all

print("... the program asks for numbers")
print(f"Numbers typed in: {all}")
print(f"The sum of the numbers is: {sum}")
print(f"The mean of the numbers is: {mean}")
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
'''''

