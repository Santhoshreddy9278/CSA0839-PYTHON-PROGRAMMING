year=int(input("enter the year"))
if(year%4==0  and year>0):
    print("the year  is leaap year")
elif(year<=0):
    print("invalid")
else:
    print("The year is not leap year")
