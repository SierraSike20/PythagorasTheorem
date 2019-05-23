print("Pythagoras Theorem Script v2")

a = str(input("Do you have the value of a hypotenuse?"))
if a.lower().strip()== "yes":
    a2 = int(input("What is the value of one of your adjacents?"))
    h = int(input("What is the value of your hypotenuse?"))
    a1 = ((h**2) - (a2**2))
    ans1 = (a1**(1 / 2))
    print("The value of your other adjacent is", ans1)
if a.lower().strip() == "no":
    b1 = int(input("What is the value of your first adjacent?"))
    b2 = int(input("What is the value of your second adjacent?"))
    b3 = ((b1**2) + (b2**2))
    ans2 = (b3**(1 / 2))
    print("The value of your hypotenuse is", ans2)
