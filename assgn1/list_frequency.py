lst1=[]
n=int(input("enter the number of terms in list : "))
print("enter the elements of the list")

for i in range(n):
    a=input()
    if len(a)>0:
        lst1.append(a)
print("the list is: ", lst1)

b=input("enter the element whose frequency is to be counted: ")
count=0
for i in range(len(lst1)):
    for j in lst1[i]:
        if b.lower()==j.lower():
            count=count+1

print("the number of occurences of ", b , " is ",count )