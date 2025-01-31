has_good_credit = True
has_good_savings = True
has_good_salary = True
has_criminal_record = True

if has_good_credit and has_good_savings:
    print("You are eligible for a loan")


if has_good_credit or has_good_salary:
    print("You are eligible for a low interest rate")


if has_good_credit and has_good_salary and not has_criminal_record:
    print("Get the loan now")