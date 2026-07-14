num1=int(input("Enter A number: "))
ops=input("Use the operator: (+,-,*,/)= ")
num2=int(input("Enter A number: "))


if(ops=='+'):
    print("Sum= ",num1+num2)
elif(ops=='-'):
    print("Difference= ",num1-num2)
elif(ops=='*'):
    print("Product= ",num1*num2)
elif(ops=='/'):
    if num2 != 0:
        print("Division= ",num1/num2) 
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")      