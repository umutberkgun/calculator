import calculatormodule


print("""

THIS IS A CALCULATOR

OPERATIONS ARE SIMPLE BECAUSE I DON'T KNOW MUCH ABOUT MATHS

CHOOSE THE OPERATION

1) ADD
2) SUBTRACT
3) MULTIPLY 
4) DIVIDE
5) FACTORIAL 
6) POWER
7) SQUARE ROOT
8) CEILING
9) ABSOLUTE
10) HYPOTENUSE

press "q" to exit


""")

x = int(input("What would you like to do? Enter the number of the operation:"))

while True:
    if x == "q":
        break
    elif x == 1:
        a = int(input("enter the number:"))
        b = int(input("enter the number:"))

        print(calculatormodule.add(a, b))

        break


    elif x == 2:
        a = int(input("enter the number:"))
        b = int(input("enter the number:"))

        print(calculatormodule.substract(a, b))
        break

    elif x == 3:
        a = int(input("enter the number:"))
        b = int(input("enter the number:"))

        print(calculatormodule.multiply(a, b))
        break
    elif x == 4:
        a = int(input("enter the number:"))
        b = int(input("enter the number:"))

        print(calculatormodule.divide(a, b))
        break
    elif x == 5:
        a = int(input("enter the number:"))


        print(calculatormodule.factorial(a))
        break
    elif x == 6:
        a = int(input("enter the number:"))

        print(calculatormodule.power(a))
        break
    elif x == 7:
        a = int(input("enter the number:"))

        print(calculatormodule.squareroot(a))
        break
    elif x == 8:
        a = int(input("enter the number:"))

        print(calculatormodule.upperint(a))
        break

    elif x == 8:
        a = int(input("enter the number:"))


        print(calculatormodule.absolute(a))
        break
    elif x == 10:
        a = int(input("enter the number:"))
        b = int(input("enter the number:"))

        print(calculatormodule.hypotenuse(a, b))
        break
































