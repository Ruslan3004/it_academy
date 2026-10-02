# HW_07_3 Higher-order functions Exercise 3.1

def apply_test_check(check_func, test_results):
    passed_count = sum(check_func(tests) for tests in test_results)
    return passed_count


test_results = [
    {"ststus": "passed"},
    {"ststus": "failed"},
    {"ststus": "passed"}
]

result = apply_test_check(
    lambda tests: tests["ststus"] == "passed", test_results)
print(f"Total tests: {result}")


# HW_07_3 Higher-order functions Exercise 3.2

def filter_logs(logs, filter_func):
    return [log for log in logs if filter_func(log)]


logs = [
    {"level": "INFO", "message": "Test started"},
    {"level": "ERROR", "message": "Login failed"},
    {"level": "WARNING", "message": "Timeout occurred"}
]

error_logs = filter_logs(logs, lambda log: log["level"] == "ERROR")
print("Errors: ", error_logs)


# HW_07_3 Higher-order functions Exercise 3.3

def transform_tests(tests, transform_func):
    return [transform_func(test) for test in tests]


tests = [
    {"name": "test1", "duration": 2.0},
    {"name": "test2", "duration": 3.0}
]

increased_tests = transform_tests(
    tests, lambda t: {**t, "duration": t["duration"] * 1.1})
print("Extended-time tests:", increased_tests)