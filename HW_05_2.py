# HW_05_2 Strings Exercise 7.1

fullname = " Ivanov Ivan Ivanovich"

surname = fullname.split()[0]
first_letter = fullname.split()[1][0]
second_letter = fullname.split()[2][0]
result = surname + " " + first_letter + " " + second_letter
print(result)


# HW_05_2 Strings Exercise 7.2

str_1 = input("Enter a string one: ")
len_str = len(str_1)
print(" The string length is: ", (len_str))


# HW_05_2 Strings Exercise 7.3

str_2 = input("Enter a string two: ")
print(str_2[::-1])


# HW_05_2 Strings Exercise 7.4

str_3 = input("Enter a string three: ")
print(str_3.replace(" ", ""))


# HW_05_2 Strings Exercise 7.5

str_4 = input("Enter a string four: ")
str_5 = input("Enter a string: five ")
check_str = str_4 in str_5
print(f"{check_str}")


# HW_05_2 Strings Exercise 7.6

str_6 = "We are python lerners"
search_smb = 'e'
check_smb = '#'
check_result = str_6.replace(search_smb, check_smb)
print(check_result)


# HW_05_2 Strings Exercise 7.7

str_7 = input("Enter a string seven: ")
check_str_7 = str_7.isdigit()
print(f"{check_str_7}")