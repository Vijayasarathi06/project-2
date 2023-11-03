####Project 2: count the letters
words=str(input("enter the words"))
a={}
for i in words:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
for x,y in a.items():
    print(f"{x}-{y}")

##Project 3
list1=[1,2,3] 
list1.remove(3)
list1.insert(1,3)
print(list1)
    
##Project 4 
w=float(input("enter the weight in Kg"))
h=float(input("enter the height in meter"))
BMI=w/h**2
print(BMI)
if BMI < 18.25:
    print("under weight")
elif BMI < 50:
    print("healthy weight")
else:
    print("over weight")
















  
