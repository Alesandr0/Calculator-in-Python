print ('Welcome to the calculator program!')
name = input ("What's your name?\n")
option = int(input (" 1- shut down   2- Sum\n 3- Subtraction   4- Division\n"))
condition = True
while condition == True:
    if(option==1):
        print ("Welcome {}".format(name))
        break
    elif (option==2): 
        numberOne = int(input("Enter a number:  "))
        numberTwo = int(input("Enter a number:  "))
        result = numberOne + numberTwo
        sun = True
        while sun == True:
            option = int(input ("would like to continue the sum?\n 1- Not  (any number)- Yes\n"))
            if (option == 1):
                print ("Sum of the numbers is: {}".format(result))
                sun= False
            else:
                numberOne = int(input('Enter a number:  '))
                result += numberOne
    elif (option == 3):
        numberOne = int(input("Enter a number:  "))
        numberTwo = int(input("Enter a number:  "))
        result = numberOne - numberTwo
        subtraction = True
        while subtraction == True:
            option = int(input ("would like to continue the sum?\n 1- Not  (any number)- Yes\n"))
            if (option == 1):
                print ("Subtraction of the numbers is: {}".format(result))
                subtraction = False
            else:
                numberOne = int(input('Enter a number:  '))
                result -= numberOne
    elif (option == 4):
        numberOne = int (input("Enter a number:  "))
        numberTwo = int (input("It will divide by how much?  "))
        result = numberOne / numberTwo
        print ("Division of the numbers is: {}".format(result))
    option = int(input (" 1- shut down     2- Sum\n 3- Subtraction   4- Division\n"))