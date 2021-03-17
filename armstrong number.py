n = int(input("Enter number: "))
sum = 0
a = n
while a>0:
    dig = a%10
    sum = sum+(dig)**3
    a = a//10
if sum == n:
    print("Armstrong")
else:
    print("Not armstrong")