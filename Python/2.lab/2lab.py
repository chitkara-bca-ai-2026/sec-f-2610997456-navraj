

employee_name = input("enter employee name: ")
print("data type:", type(employee_name))

employee_id = int(input("enter employee id: "))
print("data type:", type(employee_id))

salary = float(input("enter salary: "))
print("data type:", type(salary))

department = input("enter department: ")
print("data type:", type(department))

active_input = input("is the employee active? (yes/no): ")
active = active_input == "yes"
print("data type:", type(active))

print(f"--- employee details --- \nname       : {employee_name}\nid         : {employee_id}\nsalary     : {salary}\ndepartment : {department}\nactive     : {active}")
