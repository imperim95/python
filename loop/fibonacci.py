num1=0
num2=1

para=int(input("Dime un número: "))

for a in range(1,para+1):
    print(num2)
    num2=num2+num1
    num1=num2
print(num2)