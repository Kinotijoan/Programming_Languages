# JOAN NKATHA KINOTI
# SCT 211-0042/2022

print("WELCOME TO YOUR TRUSTED BMI CALCULATOR !")
user_weight = float(input("Enter your weight in kilograms: "))
user_height = float(input("Enter your height in centimetres: "))
height = user_height / 100

BMI = user_weight / (height ** 2)

if BMI < 18.5:
    print("Your BMI is {} and you are underweight".format(BMI))
elif 18.5 <= BMI < 25:
    print("Your BMI is {} and you are normal weight".format(BMI))
elif 25 <= BMI < 30:
    print("Your BMI is {} and you are overweight".format(BMI))
else:
    print("Your BMI is {} and you are obese".format(BMI))
