
#Additon Function
def Addition(num1,num2): 
    add=num1+num2
    return add 

#Subtraction Function
def Subtraction(num1,num2):
    sub=num1-num2 
    return sub  

#Multiplication Function
def Multiplication(num1,num2):
    multiply=num1*num2 
    return multiply 

#Division Function 
def Division(num1,num2): 
    if num2==0:
       div="Invalid Input"
    else:
        div=num1/num2

    return div






#Getting inputs form the user 
number_1=int(input("Give your First number: ")) 
number_2=int(input("Give your Second number: ")) 
operator=input("Give an operation choice: ") 

#Doing Addition function 
if (operator=="+"):
    result=Addition(number_1,number_2) 
    print("Addtion of two numbers is: "+str(result)) 
elif(operator=="-"):
    result=Subtraction(number_1,number_2) 
    print("The Subration of two numbers is: "+str(result)) 
elif(operator=="*"):
    result=Multiplication(number_1,number_2)
    print("Multiplication of two numbers is: "+str(result)) 
else:
    result=Division(number_1,number_2)
    print("Division of two numbers is: "+str(result))

