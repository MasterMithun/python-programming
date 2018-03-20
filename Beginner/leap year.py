
year1=int(input("Enter year to be checked:"))
if(year1%4==0 and year1%100!=0 or year1%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")  
