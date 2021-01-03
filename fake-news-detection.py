import math # Import math Library

print(" ***** Unit Calculator Program ***** ")
print(" "," ")

def Addition(x , y):
    return x+y
def Subtraction(x,y):
    return x-y
def Multiplication(x , y):
    return x*y
def Division(x,y):
    return x/y
def Factorial(num,factorial):
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)
def Power(x,y):
    return (pow(x,y))
def Log(x):
    return (math.log(x,2))
def natural_Log(x):
    return (math.log(x))
def Menu():
    while True:
        print(" ")
        print(" ")
        print(" **** Select Operation **** ")
        print("1.Addition ")
        print("2.Subtraction ")
        print("3.Multiplication ")
        print("4.Division ")
        print("5.Factorial ")
        print("6.Take_Power ")
        print("7.Log ")
        print("8.Natural_Log ")
        print("9.Exit")

        choice=input(" Enter any number to select operation (1/2/3/4/5/6/7/8/9) : ")

        if choice in('1','2','3','4','5','6','7','8','9'):
            print(" "," ")
            if choice == '1':
                print(" **** Addition **** ")
                num1 = float(input("Enter First Number : "))
                num2 = float(input("Enter Second Number : "))
                print(num1,"+",num2,"=",Addition(num1,num2))
            elif choice == '2':
                print(" **** Subtraction **** ")
                num1 = float(input("Enter First Number : "))
                num2 = float(input("Enter Second Number : "))
                print(num1,"-",num2,"=",Subtraction(num1,num2))
            elif choice == '3':
                print(" **** Multiplication **** ")
                num1 = float(input("Enter First Number : "))
                num2 = float(input("Enter Second Number : "))
                print(num1,"*",num2,"=",Multiplication(num1,num2))
            elif choice == '4':
                print(" **** Division **** ")
                num1 = float(input("Enter First Number : "))
                num2 = float(input("Enter Second Number : "))
                print(num1,"/",num2,"=",Division(num1,num2))    
            elif choice == '5':
                print(" **** Factorial **** ")
                num = int(input("Enter Number : "))
                print(Factorial(num,1))
            elif choice == '6':
                print(" **** Take Power **** ")
                num1 = int(input("Enter First Number : "))
                num2 = int(input("Enter Second Number : "))
                print(num1,"Power",num2,"=",Power(num1,num2))
            elif choice == '7':
                print(" **** Log **** ")
                num = int(input("Enter Number : "))
                print("Log Of",num,"is",Log(num))                
            elif choice == '8':
                print(" **** Natural_Log **** ")
                num = int(input("Enter Number : "))
                print("Natural Log Of",num,"is",natural_Log(num))
            if choice == '9':
                break

while True:
    print(" **** Select Operation **** ")
    print("1.Menu")
    print("2.Exit ")

    choice=input(" Enter any number to select operation (1/2) : ")

    if choice in('1','2'):
        if choice == '1':
            print(Menu()," "," ")
        elif choice == '2':
            break  
