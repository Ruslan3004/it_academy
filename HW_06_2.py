# HW_06_2 Loops Exercise 1

test_str = input("Enter a string 'test123': ")
len_test_str = len(test_str)
for i in range(len_test_str):
    print(test_str[i])


# HW_06_2 Loops Exercise 3

test_case = input("Enter a text 'Login Logout SignUp': ")
name_test_case = test_case.split()
for i in name_test_case:
    print(" Test case: ", i)


# HW_06_2 Loops Exercise 4

correct_password = 'admin'

while True:
    enter_pass = input("Enter a password: ")
    if enter_pass == correct_password:
        print("Pass is correct")
        break
    else:
        print("Incorrect password")


# HW_06_2 Loops Exercise 5

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

# HW_06_2 Loops Exercise 6

total_sum = 0
for i in range(1, 101):
    total_sum += i
    print("Total sum:", total_sum)


# HW_06_2 Loops Exercise 7

browsers = ['Chrome', 'Firefox']
operating_systems = ['Windows', 'Linux']
for x in browsers:
    for y in operating_systems:
        print(f'{x} - {y}')


# HW_6 Loops Exercise 8

index_str = "abc"
for index, symbol in enumerate(str):
    print([index], symbol)


# HW_06_2 Loops Exercise 9

str_email = ["user@example.com", "userexample.com"]
check_symbol = '@'
for symbol in str_email:
    if check_symbol in symbol:
        print(f"String str_email '{symbol}' has symbol '@' ")
    else:
        print(f"String str_email '{symbol}' doesn't have a symbol '@' ")


# HW_06_2 Loops Exercise 10

i_down = 10
while i_down > 0:
    i_down -= 1
    print(i_down)


# HW_06_2 Loops Exercise 11

str_pt = "Python"
for i in str_pt.upper():
    print(i, end="")


# HW_06_2 Loops Exercise 12

i_value = 0
while i_value <= 10:
    user_number = float(input("Enter a number: "))
    if user_number > 10:
        print("Error")
        break
    print(" Try again")
    i_value += 1


# HW_06_2 Loops Exercise 13

text_user = "one two three"
text_words = text_user.split()
count = 0
for i in text_words:
    count += 1
print("Word count: ", count)


# HW_06_2 Loops Exercise 14

for i in range(1, 21):
    print(i, end=" ")
    if i == 15:
        print("Error")
        break