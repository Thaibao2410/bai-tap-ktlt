# lập trình tạo một máy tính đơn giản có thể cộng, trừ, nhân và chia bằng các hàm
#this function adds two numbers
def add(x,y):
    return x + y
#This funcition subtracts two numbers 
def subtract(x, y):
    return x - y
#This function multiplies two numbers
def multipply(x,y ):
    return x*y
#This function divides two numbers
def divide(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Take input from the user
choice=input("Enter choise(1/2/3/4):")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))


if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",divide(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2)) 
else:
    print("Invalid input")                     
print("nguyễn thái bảo")   
print("MSSV: 235752020710028") 