print(__name__)
def checkNumberIsPosOrNeg():

    endFlag=False
    while endFlag==False:
        num = int(input("Enter the number: "))
        if num<0:
            print("The number is negative")
        elif num>0:
            print("The number is positive")
        else:
            print("The number is zero")

        ui = input("Would you like to repeat the program again? (Y/N): ")
        if ui.lower()=='n':
            endFlag=True
        else:
            endFlag=False
print("Hello")

def testTheModuleCalling(name):
    print("My name is "+name)
