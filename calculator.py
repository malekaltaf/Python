#calculator using python
print("Welcome To Python Calculator")
print("Please Enter Two Numbers To Calculate")
no1 = int(input("Enter First No,: "))
no2 = int(input("Enter Second No,: "))
print("Choose What You Want 'sub' 'avg' 'mul' 'div' 'add' ")
value = input("Enter Choice.:  ")
if(value == "sub"):
    print("Your Answer is.: ",no1-no2)        
elif value == "avg":
    print("Your Answer is.: ",no1+no2/2)        
elif value == "mul":
    print("Your Answer is.: ",no1*no2)        
elif value == "div":
    print("Your Answer is.: ",no1/no2)        
elif value == "add":
    print("Your Answer is.: ",no1+no2)
else:
    print("Enter Valid Input")

    
