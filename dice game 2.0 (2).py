player1score=0
player2score=0
theround=1
import time
sentence="Welcome to the dice game"
for char in sentence:
    time.sleep(0.05)
    print(char,end='')
print(".")
user1=input("What is player 1's username?")
user2=input("What is player 2's username?")
line="Your usernames have been authorised"
for char in line:
    time.sleep(0.05)
    print(char,end='')
print(".")
while theround <6 and player1score>=0 and player2score>=0:
    from random import randint
    player1= ["1", "2", "3", "4", "5", "6"]
    roll = player1[randint(0,5)]
    rolling="rolling.................."
    for char in rolling:
        time.sleep(0.05)
        print(char,end='')
    print(".")
    print(user1," has rolled a:",roll)
    if roll == "1":
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif roll == "2":
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif roll == "3":
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif roll == "4":
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif roll == "5":
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif roll == "6":
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    roll=int(roll)
    player1score=player1score + roll
    from random import randint
    player1= ["1", "2", "3", "4", "5", "6"]
    rolltwo = player1[randint(0,5)]
    rolling1="rolling.................."
    for char in rolling1:
        time.sleep(0.05)
        print(char,end='')
    print(".")
    print (user1,"has also rolled a:",rolltwo)
    if rolltwo == "1":
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif rolltwo == "2":
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif rolltwo == "3":
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif rolltwo == "4":
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif rolltwo == "5":
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif rolltwo == "6":
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    rolltwo=int(rolltwo)
    player1score=player1score + rolltwo
    if player1score%2==0:
        player1score=player1score + 10
        if roll==rolltwo:
            print(user1,"gets another roll")
            from random import randint
            player1= ["1", "2", "3", "4", "5", "6"]
            rollthree = player1[randint(0,5)]
            rolling2="rolling.................."
            for char in rolling2:
                time.sleep(0.05)
                print(char,end='')
            print(".")
            print (user1,"1 has rolled a:",rollthree)
            if rollthree == "1":
                print("[-----]")
                print("[     ]")
                print("[  0  ]")
                print("[     ]")
                print("[-----]")
            elif rollthree == "2":
                print("[-----]")
                print("[ 0   ]")
                print("[     ]")
                print("[   0 ]")
                print("[-----]")
            elif rollthree == "3":
                print("[-----]")
                print("[     ]")
                print("[0 0 0]")
                print("[     ]")
                print("[-----]")
            elif rollthree == "4":
                print("[-----]")
                print("[0   0]")
                print("[     ]")
                print("[0   0]")
                print("[-----]")
            elif rollthree == "5":
                print("[-----]")
                print("[0   0]")
                print("[  0  ]")
                print("[0   0]")
                print("[-----]")
            elif rollthree == "6":
                print("[-----]")
                print("[0 0 0]")
                print("[     ]")
                print("[0 0 0]")
                print("[-----]")
            rollthree=int(rollthree)
            player1score=player1score + rollthree
    elif player1score%2!=0:
        player1score=player1score - 5
        if roll==rolltwo:
            print(user1,"gets another roll")
            from random import randint
            player1= ["1", "2", "3", "4", "5", "6"]
            rollthree = player1[randint(0,5)]
            rolling2="rolling.................."
            for char in rolling2:
                time.sleep(0.05)
                print(char,end='')
            print(".")
            print (user1,"1 has rolled a:",rollthree)
            if rollthree == "1":
                print("[-----]")
                print("[     ]")
                print("[  0  ]")
                print("[     ]")
                print("[-----]")
            elif rollthree == "2":
                print("[-----]")
                print("[ 0   ]")
                print("[     ]")
                print("[   0 ]")
                print("[-----]")
            elif rollthree == "3":
                print("[-----]")
                print("[     ]")
                print("[0 0 0]")
                print("[     ]")
                print("[-----]")
            elif rollthree == "4":
                print("[-----]")
                print("[0   0]")
                print("[     ]")
                print("[0   0]")
                print("[-----]")
            elif rollthree == "5":
                print("[-----]")
                print("[0   0]")
                print("[  0  ]")
                print("[0   0]")
                print("[-----]")
            elif rollthree == "6":
                print("[-----]")
                print("[0 0 0]")
                print("[     ]")
                print("[0 0 0]")
                print("[-----]")
            rollthree=int(rollthree)
            player1score=player1score + rollthree
    from random import randint
    player2= ["1", "2", "3", "4", "5", "6"]
    aroll = player2[randint(0,5)]
    rolling3="rolling.................."
    for char in rolling3:
        time.sleep(0.05)
        print(char,end='')
    print(".")
    print (user2,"has rolled a:",aroll)
    if aroll == "1":
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif aroll == "2":
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif aroll == "3":
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif aroll == "4":
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif aroll == "5":
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif aroll == "6":
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    aroll=int(aroll)
    player2score=player2score + aroll
    from random import randint
    player2= ["1", "2", "3", "4", "5", "6"]
    arolltwo = player2[randint(0,5)]
    rolling4="rolling.................."
    for char in rolling4:
        time.sleep(0.05)
        print(char,end='')
    print(".")
    print (user2,"has also rolled a:",arolltwo)
    if arolltwo == "1":
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif arolltwo == "2":
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif arolltwo == "3":
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    elif arolltwo == "4":
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif arolltwo == "5":
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif arolltwo == "6":
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    arolltwo=int(arolltwo)
    player2score=player2score + arolltwo
    if player2score%2==0:
        player2score=player2score + 10
    elif player2score%2!=0:
        player2score=player2score - 5
    elif aroll==arolltwo:
        print(user2,"gets another roll")
        from random import randint
        player2= ["1", "2", "3", "4", "5", "6"]
        arollthree = player2[randint(0,5)]
        rolling5="rolling.................."
        for char in rolling5:
            time.sleep(0.05)
            print(char,end='')
        print(".")
        print (user2,"1 has rolled a:",arollthree)
        if arollthree == "1":
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif arollthree == "2":
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        elif arollthree == "3":
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        elif arollthree == "4":
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif arollthree == "5":
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        elif arollthree == "6":
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
        arollthree=int(arollthree)
        player2score=player2score + arollthree
    print("This is",user1,"score",player1score)
    print("This is",user2,"score",player2score)
    if player1score>player2score:
        player1score=str(player1score)
        writefile=open("topscores.csv","a+")
        writefile.write(user1 + "," + "your winning score is: " + player1score + "\n")
        writefile.close
    elif player1score<player2score:
        player2score=str(player2score)
        writefile=open("topscores.csv","a+")
        writefile.write(user2 + "," + "your winning score is: " + player2score + "\n")
        writefile.close
    player1score=int(player1score)
    player2score=int(player2score)
    theround=theround+1
    if theround<6 and player1score>=0 and player2score>=0:
        print("lets play round:",theround)
if player1score<0:
    print(user1,"has lost")
    print(user2,"has won")
elif player2score<0:
    print(user2,"has lost")
    print(user1,"has won")
elif theround>5:
    if player1score>player2score:
        print("congratulations",user1,"is the winner of round:",theround)
        sentence1="Your winning scores have been exported to an external file"
        import time
        for char in sentence1:
            time.sleep(0.05)
            print(char,end='')
        print(".")
    elif player1score<player2score:
        print("congratulations",user2,"is the winner of round:",theround)
        sentence2="Your winning scores have been exported to an external file"
        import time
        for char in sentence2:
            time.sleep(0.05)
            print(char,end='')
        print(".")
    while player1score==player2score:
        print("both players will roll again to see who wins round:",theround)
        from random import randint
        player1= ["1", "2", "3", "4", "5", "6"]
        extraroll = player1[randint(0,5)]
        rolling6="rolling.................."
        for char in rolling6:
            time.sleep(0.05)
            print(char,end='')
        print(".")
        print (user1,"has rolled a:",extraroll)
        if extraroll == "1":
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif extraroll == "2":
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        elif extraroll == "3":
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        elif extraroll == "4":
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif extraroll == "5":
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        elif extraroll == "6":
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
        extraroll=int(extraroll)
        player1score=player1score + extraroll
        from random import randint
        player2= ["1", "2", "3", "4", "5", "6"]
        anotherroll = player2[randint(0,5)]
        rolling7="rolling.................."
        for char in rolling7:
            time.sleep(0.05)
            print(char,end='')
        print(".")
        print (user2,"has rolled a:",anotherroll)
        if anotherroll == "1":
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif anotherroll == "2":
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        elif anotherroll == "3":
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        elif anotherroll == "4":
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif anotherroll == "5":
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        elif anotherroll == "6":
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
        anotherroll=int(anotherroll)
        player2score=player2score + anotherroll
        if player1score>player2score:
            print("congratulations",user1,"is the winner of round:",theround)
            sentence3="Your scores winning have been exported to an external file"
            import time
            for char in sentence3:
                time.sleep(0.05)
                print(char,end='')
            print(".")
        if player1score<player2score:
            print("congratulations",user2,"is the winner of round:",theround)
            sentence4="Your winning scores have been exported to an external file"
            import time
            for char in sentence4:
                time.sleep(0.05)
                print(char,end='')
            print(".")
        
    
    
