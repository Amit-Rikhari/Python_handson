    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
Ele = [Rock,Paper,Scissors]


s1 = int(input("Choice an option!\n 0= Rock\n1= Paper\n 2= Scissor"))


if s1>=3 or s1 <0:
    print("You  lose as u choosed wrong number")
else:
    print(Ele[s1])
    
    s2 = random.randint(0,2)
    print(Ele[s2])
    
    if s1>=3 or s1 <0:
        print("You  lose as u choosed wrong number")
  
    elif s1==s2:
        print("Tie!!")
    elif s2>s1:
        print("You lose")
    elif s1>s2:
        print("You Win")
    elif s1==0 and s2==2:
        print(Ele[s1])
    elif s1==2 and s2==0:
        print(Ele[s1])
