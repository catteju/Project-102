import math

def addition():
    n1 = int(input("Enter The First Value"))
    n2 = int(input("Enter The Second Value"))
    res = n1+n2
    print(res)

def subtraction():
    n1 = int(input("Enter The First Value"))
    n2 = int(input("Enter The Second Value"))
    res = n1-n2
    print(res)

def multiplication():
    n1 = int(input("Enter The First Value"))
    n2 = int(input("Enter The Second Value"))
    res = n1*n2
    print(res)

def division():
    n1 = int(input("Enter The First Value"))
    n2 = int(input("Enter The Second Value"))
    res = n1/n2
    print(res)

def powers():
    n1 = int(input("Enter The Value"))
    n2 = int(input("Enter The Power"))
    res = n1**n2
    print(res)

def squareRoot():
    n1 = int(input("Enter The Value"))
    res = math.sqrt(n1)
    print(res)

def main():
    print("Hi!! This Me Calculator/nYou Can Perform The Following Functions With Me :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Powers")
    print("6. Square Root")
    n = int(input("Please Enter The Number Of The Operation You Like To Perform"))
    if (n == 1):
        addition()
    elif (n==2):
        subtraction()
    elif (n==3):
        multiplication()
    elif (n==4):
        division()
    elif (n==5):
        powers()
    elif (n==6):
        squareRoot()

main()