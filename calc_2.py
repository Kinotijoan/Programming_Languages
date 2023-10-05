# JOAN NKATHA KINOTI
# SCT 211/0042-2022

year_of_birth = int(input("Enter your year of birth:"))
current_year = int(input("Enter the current year:"))
age = current_year - year_of_birth
months = age * 12
days = age * 365

print("You are {} years old".format(age))
print("You are {} months old".format(months))
print("You are {} days old".format(days))
