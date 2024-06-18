a=int(input("enter the number : "))
sum=0
while a>0 :
    sum=sum+a%10
    a=a//10
print("sum of digits is : ",sum)