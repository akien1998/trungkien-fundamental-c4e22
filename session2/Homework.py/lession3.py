heightcm = int(input('input cm : '))
heightm  = float(heightcm/100)
kg       = float(input('input kg : '))
BMI      = kg/(heightm*heightm)

if BMI < 16:
    print('You are underweight')
elif BMI < 18.5:
    print('Underweight')
elif BMI < 25:
    print('Normal')
elif BMI < 30:
    print('Overweight')
else:
    print('Obese')