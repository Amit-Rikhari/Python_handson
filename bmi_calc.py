print("Welcome to BMI calculator\n")
w=int(input("We igh in Kgt:\n"))
h=float(input("Height in Meter:\n"))
r= w/(h**2)
res = float(r)
print(round(res,3))

if res<=18.5:
    print("You are undersweight")
elif res<=25:
    print("You are normal weight")
    
elif res<=30:
    print("You are slightly overweight")
    
    
elif res<=35:
    print("You are obese")
    
    
if res>35:
    print("You are clinically obese")
    
