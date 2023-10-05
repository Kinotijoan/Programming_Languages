# JOAN NKATHA KINOTI
# SCT 211-0042/2022

print("WELCOME TO THE LEAP YEAR CALCULATOR !")
year = int(input("What year do you wish to know if it is a leap year? "))
leap = year % 4
if leap == 0:
    print("The year {} is a leap year".format(year))
else:
    print("The year {} is not a leap year".format(year))
