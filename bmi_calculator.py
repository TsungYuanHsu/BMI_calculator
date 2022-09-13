# BMI calculator
# Reference website: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm

height = float(input('What is height(im meter)? '))
weight = float(input('What is your weight(in kg)? '))
bmi = weight / (height**2)
bmi = round(bmi, 2)
print('Your BMI is', bmi)

if bmi <= 18.5:
	print('Your body condition is "Underweight"')
elif bmi > 18.5 and bmi < 25:
	print('Your body condition is "Normal weight"')
elif bmi >= 25 and bmi < 30:
	print('Your body condition is "Over weight"')
else:
	print('Your body condition is "Obesity"')