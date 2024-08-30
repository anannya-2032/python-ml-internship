str1=input("enter the string : ")
ps=input("suffix or prefix : ")

if ps.lower()=="suffix":
    suf=input("enter the suffix: ")
    if str1[(len(str1)-len(suf)) : len(str1)].lower()==suf.lower() :
        print("the suffix is part of the string ")
    else:
        print("the string does not end with given suffix")
elif ps.lower()=="prefix":
    pre=input("enter the prefix: ")
    if str1[0:len(pre)].lower()==pre.lower():
        print("the prefix is part of string")
    else:
        print("the string does not start with given prefix")
else:
    print("invalid input")