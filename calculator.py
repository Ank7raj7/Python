# 1 Addition
# 2 Substraction
# 3 Multiplication
# 4 Division
print("select an operation to perform:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
opperation=input()
if opperation=="1":
    #1 is in doble quotes because input is always in string
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("Sum is ",str(int(num1)+int(num2)))
elif opperation=="2":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("Difference is ",str(int(num1)-int(num2)))
elif opperation=="3":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("Product is ",str(int(num1)*int(num2)))
elif opperation=="4":
    num1=input("Enter first number:")
    num2=input("Enter second number:")
    print("The result is",str(int(num1)/int(num2)))
else:
    print ("Opperation cannot be performed")
   
      
