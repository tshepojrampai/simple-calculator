#Function for addition
def add(num1,num2):
    return (num1+num2)

#Function for subtraction
def subtract(num1,num2):
    return (num1-num2)
#Simple calculator program

#Function for multiplication
def multiply(num1,num2):
    return (num1*num2)

#Function for devision
def devide(num1,num2):
    return (num1/num2)

    
 
#Prompt user for input

num1= float(input("Enter a number: "))
operator= input("Enter operator: ")
num2= float(input("Enter a number: "))    

if operator == "+":
    print("Your answer is: ", add(num1,num2))
elif operator == "-":
    print("Your answer is: ",subtract(num1,num2))
elif operator == "*":
    print("Your answer is: ",multiply(num1,num2))
elif operator == "/":
    print("Your answer is: ", devide(num1,num2))
else:
    print("Invalid operator")
