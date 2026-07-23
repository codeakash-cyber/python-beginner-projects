import random

rolled=0
while True:

    choice=input("<------Roll the dice? (y/n)------>").lower()
    if choice=="y":
        a= random.randint(1,6)
        b= random.randint(1,6)
        total=a+b
        print(f"1st Dice : {a}\n2nd Dice : {b}\nTotal : {total}")
        rolled+=1
       
        if a==6 and b==6:
            print("🎉 JACKPOT! Double Sixes!.")
        elif a==b:
           print("Wow!, You rolled doubles!.")
        elif total==7:
           print("Lucky Seven!")

    elif choice=="n":
       print("Thank You!")
       print(f"You rolled: {rolled} times\n.")
       break

    else:
     print("Invalid Choice")

