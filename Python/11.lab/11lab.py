username = input("enter your username: ")
password = input("enter your password: ")

length_check = len(password) >= 8
digit_check = any(ch.isdigit() for ch in password)
uppercase_check = any(ch.isupper() for ch in password)

print("\n========== account security check ==========")
print(f"username : {username}")
print(f"password : {'*' * len(password)}")

print("\n------------- validation results ------------")
print(f"minimum 8 characters : {'passed' if length_check else 'failed'}")
print(f"contains a digit     : {'passed' if digit_check else 'failed'}")
print(f"uppercase letter     : {'passed' if uppercase_check else 'failed'}")

print("\n---------------- final status ---------------")

if length_check and digit_check and uppercase_check:
    print("password status : valid")
    print(f"account created successfully for {username}!")
else:
    print("password status : invalid")
    print("please try again with a stronger password.")

print("=============================================")