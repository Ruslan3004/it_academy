# HW_07_4 Arbitrary arguments Exercise 4.1

def generate_report(title, *test_names, format="html", **options):
    print(f"Report: {title}")
    print(f"Format: {format}")
    print(f"Tests: {', '.join(test_names)}")

    for key, value in options.items():
        print(f"{key}: {value}")


generate_report(
    "Daily Report",
    "test1",
    "test2",
    "test3",
    format="pdf",
    author="Tester"
)