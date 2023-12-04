def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Please select an operation code: ")
print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiply")
print("Press 4 to divide")
print("Press 5 to stop")

while True:
    choice = input("Please enter your choice \n")
    
    if choice == "5":
        break
    
    num1 = float(input("Please enter the firt number \n"))
    num2 = float(input("Please enter the second number \n"))
        
    if choice == "1" :
        print(num1,"+",num2,"=",add(num1,num2))
    
    elif choice == "2":
        print(num1,"-",num2,"=",sub(num1,num2))
    
    elif choice == "3":
        print(num1,"*",num2,"=",mult(num1,num2))
    
    elif choice == "4" and num2 != 0:
        print(num1,"/",num2,"=",divide(num1,num2))
    
    else:
        print("Invalid Input")
