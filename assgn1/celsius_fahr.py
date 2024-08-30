temp=int(input("enter the temperature w/o unit: "))
unit=input("enter the unit of temperature(C/F) : ")
if unit.lower()=="c":
    f= temp*1.8 +32
    print("the temperature in fahrenheit is ", f)
elif unit.lower()=="f":
    c=(temp-32)/1.8
    print("the temperature in celsius is ", c)
else:
    print("incorrect unit")