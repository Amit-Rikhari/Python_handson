print('''
Welcome to Love calculator\n
88                                     
88                                     
88                                     
88  ,adPPYba,  8b       d8  ,adPPYba,  
88 a8"     "8a `8b     d8' a8P_____88  
88 8b       d8  `8b   d8'  8PP"""""""  
88 "8a,   ,a8"   `8b,d8'   "8b,   ,aa  
88  `"YbbdP"'      "8"      `"Ybbd8"'  
''')

name_a= input("your name:\n")
name_b= input("Your lover's name:\n")
comb= name_a+name_b
combined=comb.lower()
t= combined.count("t")
r= combined.count("r")
u= combined.count("u")
e= combined.count("e")
first_name= t+r+u+e
l= combined.count("l")
o= combined.count("o")
v= combined.count("v")
e= combined.count("e")
second_name= l+o+v+e

first_name = str(first_name)
second_name = str(second_name)
love_score = int(first_name+second_name)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
