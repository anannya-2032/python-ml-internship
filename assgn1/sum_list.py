lst1=[]
n=int(input("enter the number of terms of list: "))
print("enter the elements: ")
sum=0
for i in range(n):
    num=int(input())
    lst1.append(num)
    sum=sum+num
print("list is : ", lst1)
print("the sum of numbers is: ", sum)