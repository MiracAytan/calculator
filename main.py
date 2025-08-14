import math
from operations.addition import add
from operations.subtraction import sub
from operations.multiplication import multi     #Import functions from other dile
from operations.division import div
from operations.base import base

def main():
    print("Calculator")
    print("Select:")
    print("1-Addition (+)")             #Choose operation with numbers
    print("2-Subtraction (-)")
    print("3-Multiplication (*)")
    print("4-Division (/)")
    print("5-Base (**)")
   

    choice = int(input("Enter choice (1/2/3/4/5): "))

    if choice > 5 or choice < 1:
        print("Choice should be between 1 and 6")
        return main()  # Yeniden başlat
    
    
    
    try:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))         #Input numbers
    except ValuError:
        return "Please enter float"             #If input isnt number it warns
    
    if choice == "1":
        result = add(num1,num2)
    elif choice == "2":                         #Make a choice
        result = sub(num1,num2)
    elif choice == "3":
        result = multi(num1,num2)
    elif choice == "4":
        result = div(num1,num2)             
    elif choice == 5:
        result = base(num1, num2)
    

    else:
        return "Invalid Choice"
    
    print(f"Result: {result}")

    
if __name__ == "__main__":      
        main()
