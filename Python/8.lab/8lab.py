student_name = input("enter student name: ")
roll_number = int(input("enter roll number: "))

print("\nenter marks for 5 subjects (0-100)")

total_marks = 0
failed = False

for i in range(1, 6):
    marks = float(input(f"enter marks for subject {i}: "))

    if marks < 0 or marks > 100:
        print("invalid marks! enter marks between 0 and 100.")
        exit()

    total_marks += marks

    if marks < 40:
        failed = True

percentage = (total_marks / 500) * 100

if failed:
    result = "fail"
    grade = "f"
    remarks = "failed in one or more subjects"
elif percentage >= 90:
    result = "pass"
    grade = "a+"
    remarks = "outstanding"
elif percentage >= 80:
    result = "pass"
    grade = "a"
    remarks = "excellent"
elif percentage >= 70:
    result = "pass"
    grade = "b"
    remarks = "very good"
elif percentage >= 60:
    result = "pass"
    grade = "c"
    remarks = "good"
elif percentage >= 50:
    result = "pass"
    grade = "d"
    remarks = "satisfactory"
else:
    result = "pass"
    grade = "e"
    remarks = "pass"

print("\n+--------------------------------------+")
print("|           academic report            |")
print("+--------------------------------------+")
print(f"| student name : {student_name:<21} |")
print(f"| roll number  : {roll_number:<21} |")
print("+--------------------------------------+")
print(f"| total marks  : {total_marks:<21.1f} |")
print(f"| percentage   : {percentage:<20.2f}% |")
print(f"| result       : {result:<21} |")
print(f"| grade        : {grade:<21} |")
print(f"| remarks      : {remarks:<21} |")
print("+--------------------------------------+")