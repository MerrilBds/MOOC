'''''
number = 2

while number < 30:
    if number % 2 == 0:
        print(number)
        number += 2

print(30)
'''''

'''''
print("Are you ready?")
number = int(input("Please type in a number: "))
while number >0:
    print(number)
    number -= 1
print("Now!")
'''''
'''''
upper_limit = int(input("Upper limit:"))
i = 1
while i<upper_limit:
    print(i)
    i+=1
'''''
'''''
upper_limit=int(input("Upper limit:"))
i = 1

while i <= upper_limit:
    print(i)
    i *=2
'''''
'''''
upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))

count = 0
result = 1

while result <= upper_limit:
    print(result)
    count += 1
    result = base ** count
'''''
'''''
#The sum of consecutive numbers, version 1
limit = int(input("Limit: "))
sum = 0
i = 1
while sum < limit:
    sum += i
    i += 1
print(sum)
'''''
'''''
#The sum of consecutive numbers, version 2
limit = int(input("Limit: "))
sum = 0
i = 1
calculation = ""
while sum < limit:
    if calculation:
        calculation += " + "
    calculation += str(i)
    sum += i
    i += 1
calculation += " = " + str(sum)
print("The consecutive sum:", calculation)

'''''
'''''
#String multipied
word = input("Please type in a string: ")
amount = int(input("Please type in an amount:"))
print(word*amount)
'''''
'''''
#The longer String
str1 = input("Please type in string 1:")
str2 = input("Please type in string 2:")
if len(str1)>len(str2):
    print(f"{str1} is longer")
elif len(str2)>len(str1):
    print(f"{str2} is longer")
else:
    print(f"The strings are equally long")
'''''
'''''
#reverse string
string = input("Please type in a string: ")
i = len(string) - 1 #dernier 
while i >= 0:
    print(string[i])
    i -= 1
'''''
'''''
#second and Second last characters
string = input("Please type in a string: ")
i = len(string) - 1 #dernier 

while i>=0:
    i -= 1
if string[1]==string[-2]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")
'''''
'''''
width = int(input("Width:"))

print(width * "#")
'''''
'''''
width = int(input("Width:"))
result = width * "#"
height = int(input("Height:"))
i = 0
while i< height:
    print(result)
    i+=1
'''''
'''''
string = input("Please type in a string:")
i = len(string) - 1
while i >= 0:
    if len(string) >= 1:
        print(string)
        print(len(string) * "-")
        string = input("Please type in a string:")
    else:
        break;
'''''
'''''
string = input("Please type in a string: ")
padding = "*" * (20 - len(string))
print(padding + string)
'''''

'''''
word = input("Word: ")
frame_width = 30
word_width = len(word)

# Calculate the number of spaces needed to center the word within the frame
left_spaces = (frame_width - word_width - 2) // 2
right_spaces = frame_width - word_width - 2 - left_spaces

# Print the top frame of asterisks
print("*" * frame_width)

# Print the middle row with the word centered
print("*" + " " * left_spaces + word + " " * right_spaces + "*")

# Print the bottom frame of asterisks
print("*" * frame_width)

'''''
'''''

string = input("Enter a string: ")
i = 1

while i <= len(string):
    # Get the substring of length i starting from the beginning of the string
    substring = string[:i]
    # Check if the first character of the substring is equal to the first character of the input string
    if substring[0] == string[0]:
        # If so, print the substring
        print(substring)
    i += 1
'''''
'''''
string = input("Enter a string: ")
i = 1

while i <= len(string):
    # Get the substring of length i ending at the end of the string
    substring = string[-i:]
    # Check if the last character of the substring is equal to the last character of the input string
    if substring[-1] == string[-1]:
        # If so, print the substring
        print(substring)
    i += 1
'''''
'''''
input_string = input("Please type in a string: ").lower()
vowels = "aeo"
found_a = False
found_e = False
found_o = False

for char in input_string:
    if char == 'a':
        print("a found")
        found_a = True
    elif char == 'e':
        print("e found")
        found_e = True
    elif char == 'o':
        print("o found")
        found_o = True

    if found_a and found_e and found_o:
        break

if not found_a:
    print("a not found")
if not found_e:
    print("e not found")
if not found_o:
    print("o not found")
'''''
'''''
# Write your solution here
# Ask user for a word and a character
word = input("Please type in a word: ")
char = input("Please type in a character: ")

# Find the index of the first occurrence of the character in the word
index = word.find(char)

# Check if the character was found and if there are at least 3 characters left after it
if index != -1 and len(word[index+1:]) >= 2:
    # Print the first three characters starting from the found index
    print(word[index:index+3])
else:
    # Print nothing if the character was not found or if there are less than 3 characters left
    print("")
'''''
'''''
number = int(input("Please type in a number:"))

third = 0
second = 0
first = 0

while first < number:
    first += 1
    second = 0
    while second < number:
        second += 1
        third = first * second
        print(f"{first} x {second} = {third}")
'''''
'''''
sentence = input("Please type in a sentence:")
words = sentence.split()
i = 0
while i < len(words):
    print(words[i][0])
    i += 1
'''''
'''''
#factorial
number = int(input("Please type in a number: "))

while number > 0:
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number  {number} is {factorial}")
    number = int(input("Please type in a number: "))

print("Thanks and bye!")
'''''
'''''
n = int(input("Please type in a number: "))
i = 1
while i <= n:
    if i == n:
        print(i)
    else:
        print(i+1)
        print(i)
    i += 2
'''''
'''''
n = int(input("Please type in a number: "))
i = 1
j = n
while i <= j:
    if i == j:
        print(i)
    else:
        print(i)
        print(j)
    i += 1
    j -= 1
'''''
'''''
#first function
def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")

if __name__ == "__main__":
    seven_brothers()
'''''
'''''
def first_character(text):
    print(text[0])
# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')
'''''
'''''
def mean(a,b,c):
    sum = a+b+c
    print(sum/3)
if __name__ == "__main__":
    mean(5, 3, 1)
    mean(10, 1, 1)
'''''
'''''
def print_many_times(text, times):
   i=1
   while i<=times:
       print(text)
       i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 3)
'''''
'''''
def hash_square(number):
    i=1
    while i<=number:
       print(number*"#")
       i+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(2)
'''''
