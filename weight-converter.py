weight = int(input("Enter your weight: "))
units = input("(L)bs or (K)g: ")
if units.upper == "L":
    kilo = int(weight / 0.453)
    print(f'Your weight is {kilo} pound')

else:
    pound = int(weight * 0.453)
    print(f'Your weight is {pound} kilo')