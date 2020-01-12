import os,time,platform
sq=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
sq1=["0","","","","","","","","","","","","","","","",""]
pA="A"
pB="B"
times=0
def main():
    times=0
    opersys=platform.system()
    if opersys =="Windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X
    global pA,pB,sq
    for i in range(1,17):
        sq[i]=str(i)
        sq1[i]=""
    pA=input("Enter Player-1 character: ")
    pB=input("Enter Player-2 character: ")
    if (pA not in sq) and (pB not in sq):
        if pA is pB:
            print("Characters must not be the same!\n")
            main()
        else:
            play()
    else:
        print("Characters must not be range 0 to 16!\n")
        main()

def play():
    board()
    if times<16:
        turn=(times%2)+1
        choose=input("Player %d choose a number between 1 and 16: "%turn)
        if choose not in sq:
            choose=""
            print(f"Invalid Move! \nPlayer {turn} turns back in 3 sec...")
            time.sleep(3)
            play()
        if turn == 1:
            mark(pA,choose)
        else:
            mark(pB,choose)
    else:
            print("The Game is draw!")
            playmore=input("Want to play again?(y/n): ").lower()
            if playmore=='y':
                main()
            else:
                print("Bye!!!")
    
def mark(player,num):
    if num == sq[int(num)]:
        sq[int(num)]=player
        sq1[int(num)]=player
        global times
        playerno=times%2+1
        result=checkWin()
        if result:
            print(f"Player {playerno} wins the game!")
            playmore=input("Want to play again?(y/n): ").lower()
            if playmore=='y':
                main()
            else:
                print("Bye!!!")
        else:
            times+=1
            play()
                
    else:
        print(f"Invalid Move! \nPlayer {playerno} turns back in 3 sec...")
        time.sleep(3)
        play()
        

def checkWin():
    res=False
    if sq[1] == sq[2] and sq[1]:
        if sq[2] == sq[3]:
            res=True
    elif sq[2] == sq[3]:
        if sq[3] == sq[4]:
            res=True
    elif sq[5] == sq[6]:
        if sq[6] == sq[7]:
            res=True
    elif sq[6] == sq[7]:
        if sq[7] == sq[8]:
            res=True
    elif sq[9] == sq[10]:
        if sq[10] == sq[11]:
            res=True
    elif sq[10] == sq[11]:
        if sq[11] == sq[12]:
            res=True
    elif sq[13] == sq[14]:
        if sq[14] == sq[15]:
            res=True
    elif sq[14] == sq[15]:
        if sq[15] == sq[16]:
            res=True
    elif sq[1] == sq[5]:
        if sq[5] == sq[9]:
            res=True
    if sq[5] == sq[9]:
        if sq[9] == sq[13]:
            res=True
    elif sq[2] == sq[6]:
        if sq[6] == sq[10]:
            res=True
    elif sq[6] == sq[10]:
        if sq[10] == sq[14]:
            res=True
    elif sq[3] == sq[7]:
        if sq[7] == sq[11]:
            res=True
    elif sq[7] == sq[11]:
        if sq[11] == sq[15]:
            res=True
    elif sq[4] == sq[8]:
        if sq[8] == sq[12]:
            res=True
    elif sq[8] == sq[12]:
        if sq[12] == sq[16]:
            res=True
    elif sq[1] == sq[6]:
        if sq[6] == sq[11]:
            res=True
    elif sq[6] == sq[11]:
        if sq[11] == sq[16]:
            res=True
    if sq[2] == sq[7]:
        if sq[7] == sq[12]:
            res=True
    elif sq[5] == sq[10]:
        if sq[10] == sq[15]:
            res=True
    elif sq[4] == sq[7]:
        if sq[7] == sq[10]:
            res=True
    elif sq[7] == sq[10]:
        if sq[10] == sq[13]:
            res=True
    elif sq[3] == sq[6]:
        if sq[6] == sq[9]:
            res=True
    elif sq[8] == sq[11]:
        if sq[11] == sq[14]:
            res=True
    return res

def board():
    opersys=platform.system()
    if opersys =="Windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X
    print(f"Player 1: {pA}\t Player 2: {pB}\n")
    print(sq1[1],"\t|",sq1[2],"\t|",sq1[3],"\t|",sq1[4])
    print("-"*8,end="|")
    print("-"*7,end="|")
    print("-"*7,end="|")
    print("-"*8)
    print(sq1[5],"\t|",sq1[6],"\t|",sq1[7],"\t|",sq1[8])
    print("-"*8,end="|")
    print("-"*7,end="|")
    print("-"*7,end="|")
    print("-"*8)
    print(sq1[9],"\t|",sq1[10],"\t|",sq1[11],"\t|",sq1[12])
    print("-"*8,end="|")
    print("-"*7,end="|")
    print("-"*7,end="|")
    print("-"*8)
    print(sq1[13],"\t|",sq1[14],"\t|",sq1[15],"\t|",sq1[16])
    print()
    
__name__==main()
