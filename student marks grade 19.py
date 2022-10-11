sub1=int(input("Enter marks of the python: "))
sub2=int(input("Enter marks of the c programming: "))
sub3=int(input("Enter marks of the maths: "))
sub4=int(input("Enter marks of the physics: "))
tot=sub1+sub2+sub3+sub4
avg=(sub1+sub2+sub3+sub4)/4
print("Total: ",tot)
print("Aggregate: ",avg)
if(avg>=75):
    print("Distinction")
elif(avg>=60 and avg<75):
    print("First division")
elif(avg>=50 and avg<60):
    print("Second division")
elif(avg>=40 and avg<50):
    print("Third division")
else:
    print("Fail")
