# HW_05_1 Data types Exercise 1

your_name = input("Enter your name: ")
print("Your name is: ")
print("Type your_name is: ", type(your_name))


# HW_05_1 Data types Exercise 2

some_number = input("Enter some number: ")
s_number = int(some_number)
print("Some number is: ", s_number)
print("Type s_number is: ", type(s_number))


# HW_05_1 Data types Exercise 3

point_number = input("Enter a number with a point (for exemple: 5.5): ")
p_number = float(point_number)
print("Point number is: ", p_number)
print("Type point_number is: ", type(p_number))


# HW_05_1 Data types Exercise 4

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
sum = first_number + second_number
print("Sum of numbers: ", sum)


# HW_05_1 Data types Exercise 5

user_string = input(" Enter a string: ")
user_list = user_string.split()
print("User list is: ", user_list)
print(" Type user_list is: ", type(user_list))


# HW_05_1 Data types Exercise 6

user_any_string = input("Enter any string: ")
print("String length is: ", len(user_any_string))


# HW_0
# 5_1 Data types Exercise 7

user_enter = input("Enter something :")
result_bool = bool(user_enter)
print("Result is: ", result_bool)
print("Type result_bool is: ", type(result_bool))


# HW_05_1 Data types Exercise 8

first_string = input("Enter first string (for example: 'Python':): ")
second_string = input("Enter second string (for example: '3.10':): ")
result_string = first_string + second_string
print("Concatenated string is: ", result_string)
print("Type result_string is: ", type(result_string))


# HW_05_1 Data types Exercise 9

enter_string = input("Enter some string: ")
user_index = int(input("Enter an index: "))
print("Symbol of string is:", enter_string[user_index])


# HW_05_1 Data types Exercise 10

enter_some_string = input("Enter some string: ")
print("The string consists of digits: ", enter_some_string.isdigit())