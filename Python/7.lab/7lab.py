year = int(input("enter year: "))

if year <= 0:
    print("\ninvalid year! please enter a positive year.")

else:
    if year % 400 == 0:
        status = "leap year"
        days_in_year = 366
        days_in_february = 29
        reason = "divisible by 400"

    elif year % 100 == 0:
        status = "common year"
        days_in_year = 365
        days_in_february = 28
        reason = "century year not divisible by 400"

    elif year % 4 == 0:
        status = "leap year"
        days_in_year = 366
        days_in_february = 29
        reason = "divisible by 4 and not a century year"

    else:
        status = "common year"
        days_in_year = 365
        days_in_february = 28
        reason = "not divisible by 4"

    print("\n========== year report ==========")
    print(f"year             : {year}")
    print(f"status           : {status}")
    print("---------------------------------")
    print(f"days in year     : {days_in_year}")
    print(f"days in february : {days_in_february}")
    print("---------------------------------")
    print(f"reason           : {reason}")
    print("=================================")
