Num1 = int(input('Enter first Number'))
Num2 = int(input('Enter second Number'))
print('Num1 + Num2 = {}\nNum1 - Num2 = {}\nNum1 * Num2 = {}\nNum1 ** Num2 = {}'.format(Num1 + Num2,Num1 - Num2,Num1 * Num2,Num1 ** Num2))
try:
    print('Num1 / Num2 = ',Num1 / Num2)
except:
    print("Yo can't divide a number by zero")
