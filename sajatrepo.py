import random

c = random.randint(1,10)

a = int(input("adj meg egy számot 1-10 között: "))

if c==a:
    print("szerencséd van")
elif c>=a:
    print("alá tippeltél")
else:
    print("fölé tippeltél")

nev = input("hogy hivnak: ")


