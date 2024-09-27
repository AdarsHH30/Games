import random
user_score=0
computer_score=0


options=["rock","paper","scissor"]


while True:
    user_choice=str(input("\n\nEnter your choice ROCK/PAPER/SCISSOR and Q for QUIT:")).lower()
    computer_choice=random.choice(options)
    
    if user_choice.lower() =="q":
        break
    
    if user_choice not in options:
        print("\nINVALID CHOICE !!!")


    elif user_choice== "rock" and computer_choice=="scissor":
        print("\nYOU WON!")
        user_score+=1 
    
        
    elif user_choice== "scissor" and computer_choice=="paper":
        print("\nYOU WON!")
        user_score+=1

    
    elif user_choice == "paper" and computer_choice=="rock":
        print("\nYOU WON!")
        user_score+=1

    elif user_choice==computer_choice:
        print("\nDRAW")
    

    else:
        print("\nCOMPUTER WON!")
        computer_score+=1
    print("COMPUTER CHOOSE:",computer_choice)
    
    
print("\nSCORE:\nYOUR SCORE:",user_score,"\nCOMPUTER SCORE:",computer_score)
print("THANKYOU FOR PLAYING !!!")