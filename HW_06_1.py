# HW_06_1 Conditional statements Exercise 1

input_first_number = float(input("Enter a number: "))

if input_first_number > 0:
    print("Positive number")
elif input_first_number == 0:
    print("Number of zero")
else:
    print("Negative number")


# HW_06_1 Conditional statements Exercise 2

end_string = input("Enter a string: ")
if not end_string.endswith("test"):
    print("String don't have 'test' ")
else:
    print("String have 'test' ")


# HW_06_1 Conditional statements Exercise 3

age = int(input("Enter your age: "))
age_check = "Access is allowd" if age >= 18 else "Access is denied"
print(age_check)


# HW_06_1 Conditional statements Exercise 4

user_text = input("Enter a text: ")
if not user_text:
    print("You didn't enter anything!")


# HW_06_1 Conditional statements Exercise 5

password = "55555"
enter_password = input("Enter a password: ")
if enter_password == password:
    print("Password is correct")
else:
    print("Password is not correct")


# HW_06_1 Conditional statements Exercise 6

some_string = input("Enter some string: ")
if "error" in some_string:
    print("Error found")
else:
    print("Error not found")


# HW_06_1 Conditional statements Exercise 7

even_number = int(input("Enter a number: "))
if even_number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# HW_06_1 Conditional statements Exercise 8

enter_text = input("Enter a text: ")
if enter_text[0].isupper():
    print("Text is correct!")
else:
    print("Text is nit correct!")


# HW_06_1 Conditional statements Exercise 9

len_string = input("Enter a srting: ")
if len(len_string) > 10:
    print(" String is long!")
else:
    print("String is short!")


# HW_06_1 Conditional statements Exercise 10

check_latter = input("Enter a latter: ")
if check_latter in 'aeiou':
    print("This is a vowel letter")
else:
    print("This is a not vowel letter")


# HW_06_1 Conditional statements Exercise 11

check_name = input("Enter a name: ")
print("Hi, student" if check_name == "Ivan" else "Incorrect")


# HW_06_1 Conditional statements Exercise 12

name = input("Enter your name: ")
surname = input("Enter your surname: ")
len_name = len(name)
len_surname = len(surname)
if len_name > len_surname:
    print("The name is longer than the surname")
else:
    print("The surname is longer than the name")


# HW_06_1 Conditional statements Exercise 13

range_number = int(input("Enter the number from 1 to 100: "))
# if 1 < range_number <= 100:
if range_number > 1 and range_number <= 100:
    print("The number in range")
else:
    print("The number not in range")


# HW_06_1 Conditional statements Exercise 14

digit_string = input("Enter a string: ")
if digit_string.isdigit():
    print("The string contains digits")
else:
    print(" The string doesn't contain digits")


# HW_06_1 Conditional statements Exercise 15

a_string = input("Enter a string: ")
if not a_string.endswith('a'):
    print("String don't have 'a' ")
else:
    print("String have 'a' ")