import math

a = 0
b = 0
c = 0


print("\nChoose mode:")
print("\n1. Find the hypotenuse of a triangle by providing its legs.")
print("\n2. Find one of the legs of a triangle by providing the other one leg and the hypotenuse.")
print("\n3. Find whether the dimentions of your right-angled triangle are correct.")
mode = input("\nInsert the number of the mode you chose:  \n")
while mode not in ["1" , "2", "3"]:
    mode = input("\nONLY 1, 2 or 3\n")

if mode == "1":
    a = int(input("\nInsert the 1st leg's value:  \n"))
    while 0 >= a:
        a = int(input("\nΤhe value of the 1st leg can't be equal or less than 0.\n"))
    b = int(input("\nInsert the 2nd leg's value:  \n"))
    while 0 >= b:
        b = int(input("\nThe value of the 2nd leg can't be equal or less than 0.\n"))
    c = math.sqrt(a**2 + b**2)
    print(f"\nThe value of the hypotenuse is {c}.\n")
elif mode == "2":
    a = int(input("\nInsert the leg's value  \n"))
    while 0 >= a:
        a = int(input("\nΤhe value of the leg can't be equal or less than 0.\n"))
    c = int(input("\nInsert the value of the hypotenuse:  \n"))
    while 0 >= c:
        c = int(input("\nΤhe value of the hypotenuse can't be equal or less than 0.\n"))
    while a >= c:
        c = int(input("\nThe value of the hypotenuse can't be equal or less than the leg's!\n If you want to change the hypotenuse's value and not the leg's value, insert the value of the hypotenuse here, or else insert the previous value). \n"))
        a = int(input("\nIf you want to change the value of the 1st leg , insert the value here, or else insert the previous value). \n"))
        
    b = math.sqrt(c**2 - a**2)
    print(f"\nThe value of the 2nd leg is {b}.\n")
else:
    a = int(input("\nInsert the 1st leg's value:  \n"))
    while 0 >= a:
        a = int(input("\nΤhe value of the 1st leg can't be equal or less than 0.\n"))
    b = int(input("\nInsert the 2nd leg's value:  \n"))
    while 0 >= b:
        b = int(input("\nΤhe value of the 2nd leg can't be equal or less than 0.\n"))
    c = int(input("\nInsert the value of the hypotenuse:  "))
    while 0 >= c:
        c = int(input("\nΤhe value of the hypotenuse can't be equal to or less than 0.\n"))
    while a >= c:
        c = int(input("\nThe value of the hypotenuse can't be equal or less than the 1st leg's! \nIf you want to change the hypotenuse's value and not the 1st leg's, insert the value of the hypotenuse here, or else insert the previous value). \n"))
        a = int(input("\nIf you want to change the 1st leg's value, insert the value here, or else insert the previous value). \n"))
    while b >= c:
        c = int(input("\nThe value of the hypotenuse can't be equal or less than the 2nd leg's! \nIf you want to change the hypotenuse's value and not the 2nd leg's, insert the value of the hypotenuse here, or else insert the previous value). \n"))
        b = int(input("\nIf you want to change the 2nd leg's value, insert the value here, or else insert the previous value) \n"))
    
    if b > a:
        d = b - a
        
    else:
        d = a - b

    e = a + b    
    
    if a**2 + b**2 == c**2 and d < c < e:
        print("\nThis is a right angled triangle!")
    else:
        print("\nIt seems that this doesn't form a right angled triangle...")
    