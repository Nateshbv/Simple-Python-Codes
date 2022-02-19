# python program for claculator
def calculator(num1, num2, operator):
    if operator=='+':  #Addition 
        return num1+num2
    elif operator=='-': # Substraction
        return num1-num2
    elif operator=='*': # Multiplication 
        return num1*num2
    elif operator=='/': # Division
        if (num2!=0):
            return num1/num2
        else:
            print("Divide by zero error")
    else:
        print("no operator or number passed")
# Define main function and the input for the calculator        
def main():
    X=float(input("enter the number 1"))
    Y=float(input("enter the number 2"))
    op=input("enter the operator")
    print(" The result of the operation is",calculator(X,Y,op))
# Call mainf function    
if __name__=="__main__":
    main()
