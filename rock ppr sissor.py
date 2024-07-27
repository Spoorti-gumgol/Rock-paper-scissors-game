import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose:  \n1.rock\n2.sissors\n3.paper")
choice = int(input("Enter ur choice: "))

comp_ch= random.randint(1,3)

if(choice == 1):
    if(choice == 1 and comp_ch==2):
        print(f"your choice: \n{rock}")
        print(f"computer choice: \n{scissors}")
        print("You win!!!")

    elif(choice == 1 and comp_ch==3):
        print(f"your choice: \n{rock}")
        print(f"computer choice: \n{paper}")
        print("You lose!!!")


    elif(choice == comp_ch):
        print(f"your choice: \n{rock}")
        print(f"computer choice: \n{rock}")
        print("Its a draw!!!")

elif(choice == 2):
    if(choice == 2 and comp_ch==3):
        print(f"your choice: \n{scissors}")
        print(f"computer choice: \n{paper}")
        print("You win!!!")


    elif(choice == 2 and comp_ch==1):
        print(f"your choice: \n{scissors}")
        print(f"computer choice: \n{rock}")
        print("You lose!!!")



    elif(choice == comp_ch):
        print(f"your choice: \n{scissors}")
        print(f"computer choice: \n{scissors}")
        print("Its a draw!!!")

elif(choice == 3):
    if(choice == 3 and comp_ch==1):
        print(f"your choice: \n{paper}")
        print(f"computer choice: \n{rock}")
        print("You win!!!")

    elif(choice == 3 and comp_ch==2):
        print(f"your choice: \n{paper}")
        print(f"computer choice: \n{scissors}")
        print("You lose!!!")

    elif(choice == comp_ch):
            print(f"your choice: \n{paper}")
            print(f"computer choice: \n{paper}")
            print("Its a draw!!!")

else:
    print("Invalid Entry!!!")