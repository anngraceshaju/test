num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
print("enter 1 for addition\n enter 2 for substraction\n enter 3 for multiplication\n enter 4 for divison")
choice=int(input())
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("invalid")

