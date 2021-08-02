#new program python
# .split()

print("Enter Below Define")
print("No1 No2 process")
print("process:..")
print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. avg")
print("6. exit")
a,b,d = [int(x) for x in input("Enter 2 No.: ").split()]
print(a,b)
if(d == 1):
    print(a+b)
elif(d == 2):
    print(a-b)
elif(d == 3):
    print(a*b)
elif(d == 4):
    print(a/b)
elif(d == 5):
    print(a+b/2)
elif(d == 6):
    exit()
else:
    print("error")
