num=int(input("enter your number : "))
flag=True
for i in range(2, num , 1):
    if num%i==0:
        flag=False
if flag==True:
    print("the number  is prime")
else:
    print("the number is composite")        