# HW_07_2 Lambda functions Exercise 2

test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2},
]


passed_test_dict = filter(lambda x: x["status"] == "passed", test_results)
passed_test_name = [x["name"] for x in passed_test_dict]

print(f"Successful tests: {passed_test_name}")


# HW_07_2 Lambda functions Exercise 2.2

tests = [
    {"name": "complex_test", "duration": 5.2},
    {"name": "simple_test", "duration": 1.1},
    {"name": "medium_test", "duration": 3.4},
]


tests.sort(key=lambda test: test["duration"])

print("Tests by execution time: ", tests)


# HW_07_2 Lambda functions Exercise 2.3

emails = ["test@gmail.com", "invalid-email", "user@company.ru", "no@domain"]


def valid(email):
    return "@" in email and (email.endswith(".com") or email.endswith(".ru"))


valid_email = list(filter(valid, emails))
print(" Valid emails: ", valid_email)