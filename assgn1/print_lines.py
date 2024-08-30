lst1=[]
str1=input("enter the string: ")
length=len(str1)
if len(str1)>0:
    lst1.append(str1)
while(length!=0):
    str2=input("string: ")
    lst1.append(str2)
    length=len(str2)

if len(lst1)==0:
    print("no element to be printed")
else:
    for i in range(len(lst1)):
        print(lst1[i])