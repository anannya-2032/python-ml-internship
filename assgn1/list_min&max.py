lst1=[]
n=int(input("enter the number of elements in the list: "))

for i in range(n):
    a=int(input())
    lst1.append(a)

print("the list is : ", lst1)
print("the max value in list is : ", max(lst1))
print("the min value in list is : ", min(lst1))
