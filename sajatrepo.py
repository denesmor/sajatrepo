import random

c = random.randint(0,10)

a = int(input("adj meg egy szamot amit négyzetre szeretnél emelni: "))
b = a**2

print(b)

if c==b:
    print("szerencséd van")
elif c>=b:
    print("alá tippeltél")
else:
    print("fölé tippeltél")


