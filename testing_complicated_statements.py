print(input("Please rank the following questions on a scale of 1-10 with 10 being the best."))

print()

loan_size = int(input("How large is the loan?"))
credit = int(input("How good is your credit history?"))
income = int(input("How high is your income?"))
down_payment = int(input("How large is your down payment?"))
should_loan = False

if loan_size >= 5:
    if credit >=7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
if loan_size < 5:
    if income >= 7 or down_payment >= 7: 
        should_loan = True
    if income >= 4 and down_payment >= 4:
        should_loan = True
    else:
        should_loan = False

print()

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. This is not a good loan.")


