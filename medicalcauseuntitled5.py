a=int(input("Enter Number of Classes Held"))
b=int(input("Enter Number Of Classes Attended"))
d=input("Any medical cause(y/n)?")
c=(b/a)*100
print("Percentage of classes attended is",c)

if(c>=75):
    print("Student is allowed to sit in exam")
elif(c<75 and d=='y'): 
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")