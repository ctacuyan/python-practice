
def daystart():
    hungry = input("Are you hungry? Yes or No?")
    if hungry.lower()=="yes":
        print("Go eat breakfast!")
        return
    if hungry.lower()=="no":
        print("Get dressed for work!")
        return
    else:
        print("Please enter yes or no")
        daystart()
daystart()

print("We are building a more complex calculator! String Edition")
num1=float(input("Enter first number"))
op=input("Which operation would you like to do?")
num2=float(input("Enter second number"))
if(op.lower()=="add"):
    print(num1+num2)
if(op.lower()=="subtract"):
    print(num1-num2)
if(op.lower()=="multiply"):
    print(num1*num2)
if(op.lower()=="divide"):
    print(num1/num2)
else:
    print("Please enter an operation command.")

print("We are building a more complex calculator! Symbol Edition")
num1=float(input("Enter first number"))
op=input("Which operation would you like to do?")
num2=float(input("Enter second number"))
if(op=="+"):
    print(num1+num2)
elif(op=="-"):
    print(num1-num2)
elif(op=="*" or op=="x"):
    print(num1*num2)
elif(op=="/"):
    print(num1/num2)
else:
    print("Please enter an operation command.")
