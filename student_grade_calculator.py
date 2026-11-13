# 1. Take student's name as input
name = input("Enter student's name: ")

# 2. Take marks of 3 subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# 3. Calculate Total Marks and Average Marks
total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

# 4. Determine the grade
if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks <= 79:
    grade = "A"
elif 60 <= average_marks <= 69:
    grade = "B"
elif 50 <= average_marks <= 59:
    grade = "C"
else:
    grade = "F"

# 5. Display the result using formatted strings (f-strings)
print(f"Student Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")