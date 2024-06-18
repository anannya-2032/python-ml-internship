a=int(input("enter the fisrt number: "))
b=int(input("enter the second number: "))
op=input("enter operation(+,-,*,/): ")

if op.strip()=="+":
    print("the sum is " , a+b)
elif op.strip()=="-":
    print("the difference is ", a-b)
elif op.strip()=="*":
    print("the product is ", a*b)
elif op.strip()=="/":
    print("the quotient is ", a/b)
else:
    print("invlaid operator")