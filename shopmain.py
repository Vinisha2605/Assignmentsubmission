a=int(input("Enter quantity"))
if(a*100 > 1000):
    print("total cost is",((a*100)-(0.1*a*100)))
else:
    print("total cost is",a*100)
    