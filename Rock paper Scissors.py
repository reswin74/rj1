def game(h,c):
    option=["rock","paper","scissors"]
    choose=random.randint(0,2)
    computer=option[choose]
    human=input("Enter your choice : ")
    print("======================================")
    print("The Human chose : {} \nThe Computer chose : {}".format(human,computer))
    if(human==computer):
        print("------Tie------")
    else:
        if(human=="rock" and computer=="scissors" ):
            print("Human wins ")
            h+=1
        elif(human=="scissors" and computer=="paper" ):
            print("Human wins ")
            h+=1
        elif(human=="paper" and computer=="rock" ):
            print("Human wins ")
            h+=1
        else:
            print("Computer wins")
            c+=1
    print("The Human score : {} \nThe Computer score : {}".format(h,c))
    print("======================================")
    if(h==5 or c==5):
        print("Match Ends")
        if(h==5):
            print("Human Won the Tournament")
        else:
            print("Machine Won the Tournament")
    else:
        game(h,c)
game(0,0)
