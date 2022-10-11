def compute_gcd(x, y):

    if x > y :
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
num=int(input("N value="))
num1 = int(input("number 1="))
num2 = int(input("number 2="))

print("The g.c.d is", compute_gcd(num1, num2))
