# This is a Calculator made by Naimish
# This is a fauty Calculator
print('''Welcome To EaSy CaLc
This program is made by Naimish

If you want to add just enter +
If you want to subtract just enter -
If you want to divide then enter /
If you want to multiply just enter *
If you want to do modulus %
If you want to get the raised to the power of enter **''')
operator = input("Enter Operator:")
num1 = input("Enter first Number:")
num2 = input("Enter second Number:")
# creating a new variable
mainopt = num1+operator+num2
print("Processing",mainopt)
if operator == "+":
    print ('Answer is', int(num1)+int(num2))
elif operator == "-":
    print ('Answer is', int(num1)-int(num2))
elif operator == "*":
    print ('Answer is', int(num1)*int(num2))
elif operator == "/":
    print ('Answer is', int(num1)/int(num2))
elif operator == "**":
    print ('Answer is', int(num1)**int(num2))
elif operator == "//":
    print ('Answer is', int(num1)//int(num2))
elif operator == "%":
    print ('Answer is', int(num1)%int(num2))
else:
    print('Unexpected error')
print('Thankyou For using this Calculator')