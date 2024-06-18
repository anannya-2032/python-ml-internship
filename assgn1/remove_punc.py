str1=input("enter the string: ")
str2=""
for i in str1:
    if i==" ":
        str2=str2+i
    elif i.isalnum() :
        str2=str2+i
print(str2)