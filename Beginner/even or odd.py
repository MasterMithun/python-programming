b= input("enter the input:")
if b.isdigit():
    if (float(b)%2==0):
        print("The given number is even")
    else:
        print("The given interger is odd")
else:    
    print("invalid entry")
