import random

random_number= random.randint(1,100)
attempts=5
count=0
print("\n-----THE NUMBER GUESSING GAME-----\n")

while attempts > count :
    x=int(input("enter a number:"))
    
    if x==random_number:
        print("correct guess! you won!!")
        print("\n-----THANK YOU FOR PLAYING-----\n")
        break
    elif x > random_number:
        print("too high.. guess a little low")
        
    elif x<random_number:
        print("too low..guess a little high")
        
    count+=1
    
if count==attempts:
    print(f'''\nthe no was {random_number}.\nyou have failed!\nstart again!\n-----THANK YOU FOR PLAYING-----''')  
    
