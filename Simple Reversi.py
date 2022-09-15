#This is a simple version of an attampt to play Reversi game with python, 
#in this version the computer's decision is not based on AI training, which is to be added in the future.

def gameover():                                       
    global score
    t2= time.time()
    time_count=str(int((t2-t1)//1))                     
    if score==0:                         
        print("GAME OVER.")
        a=0
        b=0
        for i in range(0,n):
            a=a+l[i].count(1)
            b=b+l[i].count(-1)
        score="{} to {}".format(b,a)
        print("X : O =",score)
        if a>b:
            print("O player wins.")
        elif a<b:
            print("X player wins.")
        elif a==b:
            print("Draw!")
    else:
        print("Invalid move.\nGAME OVER.\n{} player wins.".format(v))

    s0="start time,lasting seconds,board size,X player,O player,score\n"
    ss=time0+","+time_count+","+"{}*{}".format(n,n)+","+black+","+white+","+score+"\n"
    log=open("reversi.csv","a+")
    if log.read()==None:
        log.write(s0)
        log.write(ss)
    else:
        log.write(ss)
    log.close()
    input("Press ENTER to exit")
    import os
    print("log saved in:{}".format(os.getcwd()))
    import sys
    sys.exit()

def printBoard():
    i=0
    while i<n:
        print(char[i],end=" ")
        i+=1
    if i==n:
        print(char[i])
    i=1
    while i<=n:
        print(char[i],end=" ")
        for p in range(0,n-1):
            if l[i-1][p]==-1:
                print("X",end=" ")
            elif l[i-1][p]==0:
                print(".",end=" ")
            else:
                print("O",end=" ")
        if l[i-1][n-1]==-1:
            print("X")
        elif l[i-1][n-1]==0:
            print(".")
        else:
            print("O")
        i+=1

def human_move():
    global invalid_time
    position_list=check_1(player_number)
    if position_list==[]:
        if invalid_time==1:
            print("Both players have no valid move.")
            gameover()
        else:
            print("{} player has no valid move.".format(player_color))
            invalid_time=1
            computer_move()
    else:
        invalid_time=0                       
        m=""
        while True:
            m=input("Enter move for {} (RowCol):".format(player_color))
            if len(m)==2 and 0<=ord(m[0])-97<n and 0<=ord(m[1])-97<n:
                break
        x=ord(m[0])-97
        y=ord(m[1])-97
        global score
        count=0
        for i in position_list:
            if (x,y) in i:
                count+=1
                go_direction=i[1]
        if count ==0:
            score="Human gave up"
            gameover()
        else:
            flip((x,y),go_direction,player_number)
            printBoard()
            check_2()
            computer_move()
                                    
def check_1(number):
    position=[]
    for row in range(0,n):
        for col in range(0,n):
            final_direction=[]
            possible_direction=[]
            if l[row][col]==0:
                m=[]
                for e,f in direction:
                    m.append((e+row,f+col))
                mm=[]
                for i in range(0,8):
                    if 0<= m[i][0]<n and 0<= m[i][1] <n:
                        mm.append(m[i])          
                m=[]
                for i in range(0,len(mm)):
                    if l[mm[i][0]][mm[i][1]]==-1*number:
                        m.append((mm[i][0],mm[i][1]))           
                if m!=[]:
                    for i in range(0,len(m)):
                        possible_direction.append((m[i][0]-row,m[i][1]-col))  

                for xx,yy in possible_direction:
                    a=xx
                    b=yy
                    while l[row+xx][col+yy]==-1*number and 0<=row+xx+a<n and 0<=col+yy+b<n:
                        xx=xx+a
                        yy=yy+b
                    if l[row+xx][col+yy]==number:
                        final_direction.append((a,b))
            if final_direction != []:
                position.append([(row,col),final_direction])
    return position 

def check_2():
    a=0
    b=0
    c=0
    for i in range(0,n):
        a=a+l[i].count(1)
        b=b+l[i].count(0)
        c=c+l[i].count(-1)
    if a==0 or b==0 or c==0:
        gameover()                      
    
def computer_move():
    global invalid_time
    position_list=check_1(player_number*-1)
    if position_list==[]:
        if invalid_time==1:
            print("Both players have no valid move.")
            gameover()
        else:
            print("{} player has no valid move.".format(computer_color))
            invalid_time=1
            human_move()
    else:
        invalid_time=0
        import random
        random_position=random.choice(position_list)
        x=random_position[0][0]
        y=random_position[0][1]                
        CX=chr(x+97)
        CY=chr(y+97)
        flip((x,y),random_position[1],player_number*-1)
        print("Computer places {} at {}{}.".format(computer_color,CX,CY))
        printBoard()
        check_2()
        human_move()

def flip(position,direction,number): 
    x,y=position[0],position[1]
    l[x][y]=number
    for xx,yy in direction:
        a=xx
        b=yy
        while l[x+xx][y+yy]==number*-1 and 0<=x+xx+a<n and 0<=y+yy+b<n:
            l[x+xx][y+yy]=number
            xx=xx+a
            yy=yy+b    

direction= ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
import time
time0=time.strftime("%Y%m%d %H:%M:%S", time.localtime())
t1= time.time()
print("Reversi or Othello","\n","START")
import string
char=" "+string.ascii_lowercase      
n=1
print("the board dimension is an odd among 4-26")
while n%2!=0 or n>26 or n<4:
    n=int(input("Enter the board dimension:"))

score=0
invalid_time=0
l=[[0 for i in range(0,n)]for i in range(0,n)]
l[n//2][n//2]=1
l[n//2-1][n//2-1]=1
l[n//2][n//2-1]=-1
l[n//2-1][n//2]=-1                   
v=""
while v!="X" and v!="O":
    v=input("Computer plays(X/O):")
    if v=="X":
        player_color,computer_color="O","X"
        player_number=1
        white,black="human","computer"
    else:
        player_color,computer_color="X","O"
        player_number=-1
        white,black="computer","human"
printBoard()
if player_number==1:
    computer_move()
else:
    human_move()


