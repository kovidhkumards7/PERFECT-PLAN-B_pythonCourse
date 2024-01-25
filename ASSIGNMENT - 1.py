# GOOGLE LINK  -  https://cdn-dffiles.invanto.com/12946/coachrack/courses/13610/files/pythonliveclassesfinal.pdf




# Problem 1 : Python Program to add two numbers
def sum():
    firstNumber = float(input("enter number  "))
    secondNumber = float(input("enter number  "))
    return (firstNumber + secondNumber)
print("sum = ", sum())




# Problem 2 : Python Program for factorial of a number
def factorialFun():
    numberEntered = int(input("enter number  "))
    temp = numberEntered
    factorial = 1
    while(numberEntered > 0):
        factorial = factorial * numberEntered
        numberEntered = numberEntered - 1
    return (factorial)
print("factorial of ", temp, " is ", factorialFun())




# Problem 3 : Python Program for simple interest
def si():
    principleAmount = float(input("enter principal amount  "))
    time = float(input("enter time  "))
    rateOfIntrest = float(input("enter rate of intrest  "))
    simpleIntrest = ( principleAmount * time * rateOfIntrest / 100 )
    return (simpleIntrest)
print("simple intrest is  ", si())




# Problem 4 : Python Program for compound interest
def ci():
    principleAmount = float(input("enter principal amount  "))
    time = float(input("enter time  "))
    rateOfIntrest = float(input("enter rate of intrest  "))
    compoundIntrest = principleAmount * time * ( 1+ ( rateOfIntrest / 100 ) )
    return (compoundIntrest)
print("compound intrest is  ", ci())




# Problem 5 : Python Program to check Armstrong Number
import math
def amstrong():
    number = input ( "enter a number to check if it's amstrong or not  " )
    lenght = len( number )
    sum = 0
    try:
        temp = int( number )
    except:
        print( "enter a valid number" )
    temp = int( number )
    while ( temp > 0 ):
        digit = temp % 10
        sum = sum + math.pow( digit , lenght )
        temp //= 10
    print( sum )
    if (sum == int( number ) ):
        print( "it's a amstrong number" )
    else:
        print( "it's not an amstrong number" )
amstrong()




# Problem 6 : Python Program for Program to find area of a circle
def area():
    radius = float(input("enter the radius of the circle "))
    area = (22 / 7) * (radius ** 2)
    return (area)
print( "area is ", area() , " sq units" )




# Problem 7 : Python program to print all Prime numbers in an Interval
def prime():
    lowerLimit = int( input( "enter lower limit " ) )
    upperLimit = int( input( "enter upper limit " ) )
    if ( lowerLimit > 1 ) and ( upperLimit > lowerLimit ):
        for selectedNumber in range( lowerLimit , upperLimit + 1 , 1 ):
            for divisorSelected in range( 2 , selectedNumber , 1 ):
                if ( selectedNumber % divisorSelected == 0 ):
                    tempValue = 0
                    break
                else:
                    tempValue = 1
            if ( tempValue == 1 ):
                print( selectedNumber )
prime()




# Problem 8 : Python program to check whether a number is Prime or not
def primeOrNot():
    enteredNumber = int(input("enter a number > than 1 to check if it's prime or not "))
    if ( enteredNumber > 1):
        temp = 0
        for divisorSelected in range(2 , enteredNumber , 1):
            if ( enteredNumber % divisorSelected == 0):
                temp = 0
                break
            else:
                temp = 1
        if ( temp == 0):
            print( "it's not a prime number" )
        else:
            print( " it's a prime number" )
    else:
        print( "enter a valid number" )
primeOrNot()




# Problem 9 : Python Program for n-th Fibonacci number
def fibo():
    numberOfTerms = int(input("enter the number "))
    digit1 = 0
    digit2 = 1
    print(digit1, digit2, end ="\t")
    increment = 0
    while (increment < numberOfTerms - 2):
        digit3 = digit1 + digit2
        print(digit3, end ="\t")
        digit1 = digit2
        digit2 = digit3
        increment = increment + 1
fibo()




# Problem 10 : Python Program for printing Fibonacci numbers less than a user entered number
def fiboOrNot():
    numberOfTerms = int(input("enter the number "))
    digit1 = 0
    digit2 = 1
    digit3 = digit1 + digit2
    print(digit1, digit2, end ="\t")
    increment = 0
    while (digit3 < numberOfTerms):
        digit3 = digit1 + digit2
        if (digit3 < numberOfTerms):
            print(digit3, end ="\t")
        digit1 = digit2
        digit2 = digit3
        increment = increment + 1
fiboOrNot()




# Problem 11 : Python Program for How to check if a given number is Fibonacci number?
enteredNumber = int(input("enter a number "))
fibonacciList = [0 , 1]
firstTerm = 0
secondTerm = 1
thirdTerm = firstTerm + secondTerm
while (thirdTerm < enteredNumber + 1):
    thirdTerm = firstTerm + secondTerm
    fibonacciList.append(thirdTerm)
    firstTerm = secondTerm
    secondTerm = thirdTerm
for checkNumber in fibonacciList:
    if ( checkNumber == enteredNumber):
        temp = 0
        break
    else:
        temp = 1
if ( temp == 0):
    print( "it's a fibbonaci number " )
else:
    print( "it's not a fibbonaci number ")




# Problem 12 : Program to print ASCII Value of a character
userEnteredString = input("enter the string to be converted to ASCII values  ")
for trial in userEnteredString:
    print(trial, ord(trial), end ="\t")




# Problem 13 : Python Program for Sum of squares of first n natural numbers
limit = int(input("enter limit  "))
sum = 0
for instant in range(0 , limit + 1):
    sum = sum + instant
print(sum)




# Problem 14 : Python Program for squares sum of first n natural numbers
limit = int(input("enter limit  "))
sum = 0
for instant in range(0 , limit + 1):
    sum = sum + instant ** 2
print(sum)




# Problem 14 : Python Program for cube sum of first n natural numbers
n = int( input( "enter limit  " ) )
a = []
for i in range( 0 , n + 1 ):
    a.append( i )
b = [ i ** 3 for i in a ]
print( sum(b) )