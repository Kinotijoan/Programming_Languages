# JOAN NKATHA KINOTI
# SCT 211-0042/2022

user_name = input("What is your name?")
Total_bill = float(input("What is your total bill {} :".format(user_name)))
people = int(input("How many are you ? "))
print("What percentage of your bill would you like to give as tip?")
answer = input("Choose :\n a for 10%\n b for 12% \n c for 15% :")

while answer not in ['a', 'b', 'c']:
    print("Invalid choice")
    answer = input("Choose :\n a for 10%\n b for 12% \n c for 15% :")


def calculate_tip(bill, choice):
    # Calculate the tip based on the bill amount and the user's choice of tip percentage.

    ten_percent = 0.1
    twelve_percent = 0.12
    fifteen_percent = 0.15

    tip = 0

    if choice == 'a':
        tip = bill * ten_percent
    elif choice == 'b':
        tip = bill * twelve_percent
    elif choice == 'c':
        tip = bill * fifteen_percent

    print(f"Tip is {tip}")
    return tip


newTip = calculate_tip(Total_bill, answer)

total_pay = newTip + Total_bill

individual_pay = total_pay / people

print("Each person should pay: {}".format(individual_pay))
