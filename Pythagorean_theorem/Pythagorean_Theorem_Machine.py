import math

a = 0
b = 0
c = 0


print("\nChoose mode:")
print("\n1. Find the hypotenuse of a triangle by providing its legs.")
print("\n2. Find one of the legs of a triangle by providing the other one and the hypotenuse.")
print("\n3. Find whether the dimentions of your right-angled triangle are correct.")
mode = input("\nInsert the number of the mode you chose:  \n")
while mode not in ["1" , "2", "3"]:
    mode = input("\nONLY 1, 2 or 3\n")

if mode == "1":
    a = int(input("\nInsert 1st leg:  \n"))
    while 0 >= a:
        a = int(input("\nΤhe leg can't be equal  or less than 0.\n"))
    b = int(input("\nInsert 2nd leg:  \n"))
    while 0 >= b:
        b = int(input("\nThe leg can't be equal  or less than 0.\n"))
    c = math.sqrt(a**2 + b**2)
    print(f"\nThe hypotenuse is {c}.\n")
elif mode == "2":
    a = int(input("\nInsert leg:  \n"))
    while 0 >= a:
        a = int(input("\nΤhe leg can't be equal or less than 0.\n"))
    b = int(input("\nInsert hypotenuse:  \n"))
    while 0 >= b:
        b = int(input("\nΤhe hypotenuse can't be equal or less than 0.\n"))
    while a >= b:
        a = int(input("\nThe hypotenuse can't be equal or less than the legs (If you want to change the hypotenuse and not the leg, insert the value of the hypotenuse here, or else insert the previous value). \n"))
        a = int(input("\nThe hypotenuse can't be equal orl ess than the legs (If you want to change the leg, insert the value here, or else insert the previous value). \n"))
    c = math.sqrt(b**2 - a**2)
    print(f"\nThe other leg is {c}.\n")
else:
    a = int(input("\nInsert 1st leg:  \n"))
    while 0 >= a:
        a = int(input("\nΤhe leg can't be equal or less than 0.\n"))
    b = int(input("\nInsert 2nd leg:  \n"))
    while 0 >= b:
        b = int(input("\nΤhe leg can't be equal or less than 0.\n"))
    c = int(input("\nInsert hypotenuse:  "))
    while 0 >= c:
        c = int(input("\nΤhe hypotenuse can't be equal to or less than 0.\n"))
    while a >= c:
        c = int(input("\nThe hypotenuse can't be equal or less than the legs (If you want to change the hypotenuse and not the leg (1st leg), insert the value of the hypotenuse here, or else insert the previous value). \n"))
        a = int(input("\nThe hypotenuse can't be equal or less than the legs (If you want to change the legs value, insert the value here, or else insert the previous value). \n"))
    while b >= c:
        c = int(input("\nThe hypotenuse can't be equal or less than the legs (If you want to change the hypotenuse and not the leg (2nd leg), insert the value of the hypotenuse here, or else insert the previous value). \n"))
        b = int(input("\nThe hypotenuse can't be equal or less than the legs (If you want to change the legs value, insert the value here, or else insert the previous value) \n"))
    
    if b > a:
        d = b - a
        
    else:
        d = a - b

    e = a + b    
    
    if a**2 + b**2 == c**2 and d < c < e:
        print("\nThis is a right angled triangle!")
    else:
        print("\nIt seems that this doesn't form a right angled triangle...")
    