height = int(input("What is your height in CM"))
bill=0
if height>=120:
    print("You can eide the rollercoaster")
    age = int(input("Your age to calculate ur fair"))
    if age<12:
        bill =5
        print("Child ticket is $5")
    elif age<=18:
        bill = 7
        print("Youth ticket is $7")
    elif age>45 and age<55:
        bill = 0
        print("Enjoy your free ride\n")
    else:
        bill = 12
        print("Adult ticket is $12")
        wanna_photo= input("Do you want a photo taken Y or N")
    if wanna_photo =='Y':
        bill+=3
    
        print(f"Your total bill is ${bill}")

else: 
    print("Not eligible")
   