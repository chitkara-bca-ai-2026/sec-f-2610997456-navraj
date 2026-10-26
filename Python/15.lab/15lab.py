students = {
    "101": {
        "name": "aman",
        "branch": "bca ai",
        "semester": 1,
        "marks": [85, 90, 78]
    },
    "102": {
        "name": "riya",
        "branch": "bca ai",
        "semester": 1,
        "marks": [92, 88, 95]
    },
    "103": {
        "name": "karan",
        "branch": "bca ai",
        "semester": 1,
        "marks": [74, 80, 82]
    }
}

while True:
    print("\n" + "=" * 45)
    print("       student management system")
    print("=" * 45)
    print("1. view all students")
    print("2. search student")
    print("3. register new student")
    print("4. update student details")
    print("5. academic performance")
    print("6. delete student record")
    print("7. exit")
    print("=" * 45)

    choice = input("enter your choice (1-7): ")

    if choice == "1":
        print("\n" + "-" * 45)
        print("             student records")
        print("-" * 45)

        if students:
            for roll, student in students.items():
                print(f"\nroll number : {roll}")
                print(f"name        : {student['name']}")
                print(f"branch      : {student['branch']}")
                print(f"semester    : {student['semester']}")
                print(f"marks       : {student['marks']}")
                print("-" * 45)

        print("total students:", len(students))

    elif choice == "2":
        roll = input("enter roll number to search: ")
        student = students.get(roll)

        if student:
            print("\n--------- student details ---------")
            print(f"roll number : {roll}")
            print(f"name        : {student['name']}")
            print(f"branch      : {student['branch']}")
            print(f"semester    : {student['semester']}")
            print(f"marks       : {student['marks']}")
            print("-" * 35)
        else:
            print("[error] student record not found.")

    elif choice == "3":
        print("\n--------- new student registration ---------")

        roll = input("enter roll number: ")

        if roll in students:
            print("[error] roll number already exists.")
            continue

        name = input("enter student name: ").strip()
        branch = input("enter branch: ").strip()

        if not name or not branch:
            print("[error] name and branch cannot be empty.")
            continue

        try:
            semester = int(input("enter semester: "))

            if semester < 1:
                print("[error] semester must be at least 1.")
                continue

            marks = []
            valid_marks = True

            for i in range(1, 4):
                mark = int(input(f"enter marks for subject {i}: "))

                if mark < 0 or mark > 100:
                    print("[error] marks must be between 0 and 100.")
                    valid_marks = False
                    break

                marks.append(mark)

            if valid_marks:
                students[roll] = {
                    "name": name,
                    "branch": branch,
                    "semester": semester,
                    "marks": marks
                }
                print("\n[success] student registered successfully.")

        except ValueError:
            print("[error] enter valid numeric values.")

    elif choice == "4":
        roll = input("enter roll number to update: ")
        student = students.get(roll)

        if student:
            print("\n--------- update student details ---------")
            print("1. update branch")
            print("2. update semester")

            field = input("select an option: ")

            if field == "1":
                branch = input("enter new branch: ").strip()

                if branch:
                    student["branch"] = branch
                    print("[success] branch updated.")
                else:
                    print("[error] branch cannot be empty.")

            elif field == "2":
                try:
                    semester = int(input("enter new semester: "))

                    if semester >= 1:
                        student["semester"] = semester
                        print("[success] semester updated.")
                    else:
                        print("[error] semester must be at least 1.")

                except ValueError:
                    print("[error] enter a valid semester.")

            else:
                print("[error] invalid option.")

        else:
            print("[error] student record not found.")

    elif choice == "5":
        roll = input("enter roll number: ")
        student = students.get(roll)

        if student:
            total = sum(student["marks"])
            average = total / len(student["marks"])
            result = (
                "pass"
                if all(mark >= 40 for mark in student["marks"])
                else "fail"
            )

            print("\n" + "=" * 40)
            print("           academic report")
            print("=" * 40)
            print(f"student name : {student['name']}")
            print(f"roll number  : {roll}")
            print(f"subject marks: {student['marks']}")
            print("-" * 40)
            print(f"total marks  : {total} / 300")
            print(f"average      : {average:.2f}%")
            print(f"result       : {result}")
            print("=" * 40)

        else:
            print("[error] student record not found.")

    elif choice == "6":
        roll = input("enter roll number to delete: ")
        student = students.pop(roll, None)

        if student:
            print("\n--------- record deleted ---------")
            print(f"student name : {student['name']}")
            print(f"roll number  : {roll}")
            print("[success] student record deleted.")
            print("-" * 35)
        else:
            print("[error] student record not found.")

    elif choice == "7":
        print("\nthank you for using the student management system.")
        print("goodbye!")
        break

    else:
        print("[error] invalid choice. please select from 1 to 7.")