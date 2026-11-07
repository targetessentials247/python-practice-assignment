name = input("Enter student name: ")

math_marks = float(input("Enter Math marks: "))
english_marks = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))

if not (0 <= math_marks <= 100) or not (0 <= english_marks <= 100) or not (0 <= python_marks <= 100):
    print("\nError: Invalid marks entered! Marks must be between 0 and 100.")
else:
    average_marks = (math_marks + english_marks + python_marks) / 3

    # 4. Determine the grade based on average marks
    if 80 <= average_marks <= 100:
        grade = "A+"
    elif 70 <= average_marks <= 79.99:
        grade = "A"
    elif 60 <= average_marks <= 69.99:
        grade = "A-"
    elif 50 <= average_marks <= 59.99:
        grade = "B"
    elif 40 <= average_marks <= 49.99:
        grade = "C"
    else:
        grade = "F"

    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade: {grade}")