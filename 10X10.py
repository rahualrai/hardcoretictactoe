def draw_board(arr):
    """
    arr is the array of X, O, or " " as it is in the board
    """
    n = len(arr) # the length of the array - the board is an nxn board
    top = "  "  # the board has a top which has all the numbers across
    demLine = "  "
    rowLine = "" 
    for i in range(0,n):
        top += "  " + str(i) + " " # add the number markers to the top string
        demLine += "+———" # this is the demarcation between each row
    print(top) # print the top which contains the numbers across
    for i in range(0,n):
        rowLine = str(i) + " " # current row of X, O, and " ". Starts with row number
        print(demLine, end = "+\n") # print the demarcation ending w/ an * and newline 
        for j in range(0,n):
            rowLine += "| " + arr[i][j] + " " # add X, O, or " " to current row    * X * O
        print(rowLine + "|") # show the current row ending with an *
    print(demLine, end = "+\n") # print the last demarcation line at the end

def check_coord(x,n):
    """
    This function checks if a value of x or y inputed by the user to place X or 
    O in a certain location (x,y) is correct.
    Returns True if x is a valid input.
    Returns False otherwise.
    """
    try:
        int(x) # converts to integer. No error if x is an integer
    except ValueError:
        # if x is not an integer:
        print("Input an integer between 0 and " + str(n) + " inclusive")
        return False
    # if x is an interger:
    if not (0 <= int(x) < n):
        # if x is an integer but is not a valid index i.e not in 0 <= x < n
        print("Wrong coordinate input")
        return False
    else:
        # if there is no error
        return True

def play_game(n,thresh):
    global prevx,prevy
    prevy = 0
    prevx = 0

    tttboard = [] # this keeps record of the board, either X or O or " "
    plays = 0 # number of time both players have played in total

    # generate a double array of spaces as an initial board
    inner = []
    for _ in range(0,n):
        inner.append(" ")
    for _ in range(0,n):
        tttboard.append(inner[:])
      
    # To check if someone has won. If anyone wins, won is going to be
    # a  string: X wins, O wins, or DRAW
    won = None

    curr_player = True # boolean to check player 1 or 2
    draw_board(tttboard) # displays inital empty board

    while (won == None): # if won is None, no player has won
        if curr_player:
            print("Player 1") # if curr_player is true player 1 is to play
            valid_p1_location = False  # valid_p1_location tracks whether the player has chosen a valid location
            while not valid_p1_location:  # while a valid location (x,y) has not been chosen
                valid_no = False
                while not valid_no:  # while a valid x value has not been chosen
                    x = input("Input the x location: ")  # x is a string
                    valid_no = check_coord(x, n)  # check if x is an integer between 0 and n CPU NEEDED
                x = int(x)
                valid_no = False
                while not valid_no:  # while a valid y value has not been chosen
                    y = input("Input the y location: ")
                    valid_no = check_coord(y, n)  # check if y is an integer between 0 and n CPU NEEDED
                y = int(y)
                if tttboard[x][y] != " ":
                    print("Space used. Select another.")
                else:
                    valid_p1_location = not valid_p1_location  # correct location chosen... continue game
        else:
            print("CPU") # if curr_player is false player 2 is to play 
            x,y = CPU_next_move(tttboard)  #ava_location = avaiableLocation for CPU moves
            prevx = x
            prevy = y

        # the current player has to choose a location to play to

        if curr_player:
            tttboard[x][y] = "X"
            if check_win(tttboard, x, y, thresh, "X"): # check if X has won
                draw_board(tttboard)
                won = "P1 wins" # won is no longer None. While loop breaks
                continue
        else:
            tttboard[x][y] = "O"
            if check_win(tttboard, x, y, thresh, "O"): # check if Y has won
                draw_board(tttboard)
                won = "CPU wins" # won is no longer None. While loop breaks
                continue
        
        # if nobody has won
        draw_board(tttboard) # show the updated board
        plays += 1 # increase the number of those who have played
        curr_player = not curr_player  #change the player to the CPU

        # if people have played n^2 times, the whole board is filled.
        # it's a draw
        if plays == n**2:
            won = "DRAW"
        
    # this runs after won has changed to either "X wins", "O wins", or "DRAW"    
    print(won)

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

def CPU_next_move(tttboard): #Telling CPU where it can make a move/play. returns the coords of the next move
    global CPU, p1
    CPU = 'O'
    p1 = 'X'

    is_winning, posx, posy = winning_move(tttboard)
    if is_winning:
        print(f"CPU plays winning move at {posx}, {posy}")
        return posx, posy

    is_def, posx, posy = cpu_defence(tttboard)
    if is_def:
        print(f"CPU plays defence at {posx}, {posy}")
        return posx, posy

    is_attack, posx, posy = check_attack(tttboard, prevx, prevy, 5)
    if is_attack:
        print(f"CPU plays attacking move at {posx}, {posy}")
        return posx, posy 
    
    posx, posy = normal_move(tttboard)
    print(f"CPU plays normal move at {posx}, {posy}")
    return posx, posy
    
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Check Starts Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

def check_win(tttboard,x,y,tar,ch):
      if check_rows(tttboard,x,y,tar,ch):
        return True
      elif check_columns(tttboard,x,y,tar,ch):
        return True
      elif check_right_diag(tttboard,x,y,tar,ch):
        return True
      elif check_left_diag(tttboard,x,y,tar,ch):
        return True
      else: 
        return False

def check_rows(tttboard,x,y,tar,ch): #ch = X
    for i in range(y-tar+1,y+1):
        if i < 0:
            continue
        every_x = True
        for j in range(i,i+tar): #i = 1, tar = 3, ch = O, j = 1, 2, 3
            if j >= len(tttboard):
                every_x = False
                break
            if not tttboard[x][j] == ch:
                every_x = False
                break
        if every_x:
            return True
  
def check_columns(tttboard,x,y,tar,ch):
    for i in range(x-tar+1,x+1):
        if i < 0:
            continue
        every_y = True
        for j in range(i,i+tar):
            if j >= len(tttboard):
                every_y = False
                break
            if not tttboard[j][y] == ch:
                every_y = False
                break
        if every_y:
            return True

def check_right_diag(tttboard,x,y,tar,ch):
    n = len(tttboard)
    for i in range(0,tar):
        if x-i < 0 or y-i < 0:
            continue
        every_xy = True
        for j in range(0,tar):
            if j+x-i >= n or j+y-i >= n:
                every_xy = False
                break
            if not tttboard[j+x-i][j+y-i] == ch:
                every_xy = False
                break
        if every_xy:
            return True

def check_left_diag(tttboard,x,y,tar,ch):
    n = len(tttboard)
    for i in range(0,tar):
        if x+i >= n or y-i < 0:
            continue
        every_xy = True
        for j in range(0,tar):
            if x+i-j < 0 or j+y-i >= n:
                every_xy = False
                break
            if not tttboard[x+i-j][j+y-i] == ch:
                every_xy = False
                break
        if every_xy:
            return True

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Check Ends Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Attack Starts Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

def winning_move(tttboard):

    for cpux in range(len(tttboard)):
        for cpuy in range(0,len(tttboard)):
            if tttboard[cpux][cpuy] == CPU:
                
                # rows 
                win_move,posx,posy = check_win_rows(tttboard,cpux,cpuy,5)
                if win_move:
                    return True,posx,posy
                # columns |
                win_move,posx,posy = check_win_columns(tttboard,cpux,cpuy,5)
                if win_move:
                    return True,posx,posy
                # right diagonals /
                win_move,posx,posy = check_win_right_diag(tttboard,cpux,cpuy,5)
                if win_move:
                    return True,posx,posy
                # left diagonals \
                win_move,posx,posy = check_win_left_diag(tttboard,cpux,cpuy,5)
                if win_move:
                    return True,posx,posy
    
    return False, -1, -1

def test_wins(extracted):

    condi1 = [" ", CPU, CPU, CPU, CPU]
    condi2 = [CPU, " ", CPU, CPU, CPU]
    condi3 = [CPU, CPU, " ", CPU, CPU]
    condi4 = [CPU, CPU, CPU, " ", CPU]
    condi5 = [CPU, CPU, CPU, CPU, " "]

    if extracted == condi1:
        return True, 0
    elif extracted == condi2:
        return True, 1
    elif extracted == condi3:
        return True, 2
    elif extracted == condi4:
        return True, 3
    elif extracted == condi5:
        return True, 4
    else:
        return False, -1

def check_win_rows(tttboard,x,y,tar):
    for i in range(y-tar+1,y+1):
        if i < 0 or i > 5:
            continue
        extracted = []
        for j in range(i,i+tar): 
            extracted.append(tttboard[x][j])
        lst, away = test_wins(extracted)
        if lst:
            if tttboard[x][i+away] == " ":
                return True, x, i+away
    return False, -1, -1

def check_win_columns(tttboard,x,y,tar):
    for i in range(x-tar+1,x+1):
        if i < 0 or i > 5:
            continue
        extracted = []
        for j in range(i,i+tar):
            extracted.append(tttboard[j][y])
        lst, away = test_wins(extracted)
        if lst:
            if tttboard[i+away][y] == " ":
                return True, i+away, y    
    return False, -1, -1

def check_win_right_diag(tttboard,x,y,tar=5):
    for i in range(0,tar):
        if x-i > 5 or x-i < 0 or y-i < 0 or y-i > 5:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[x-i+j][y-i+j])
        lst, away = test_wins(extracted)
        if lst:
            return True, x-i+away, y-i+away 
    return False, -1, -1

def check_win_left_diag(tttboard,x,y,tar=5):
    for i in range(0,tar):
        if x+i < 0 or x-i > 5 or y+i < 0 or y+i > 5:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[x+i-j][y-i+j])
        lst, away = test_wins(extracted)
        if lst:
            return True, x-i+away, y-i+away 
    return False, -1, -1
    
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Winning Ends Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Attack Starts Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

def test(extracted):

    condi1 = [" ", CPU, CPU, CPU, " "]
    condi2 = [" ", CPU, " ", CPU, CPU]
    condi3 = [CPU, " ", CPU, CPU, " "]

    if extracted == condi1:
        return True, 0
    elif extracted == condi2:
        return True, 2
    elif extracted == condi3:
        return True, 1
    else:
        return False, -1

def check_attack(tttboard,x,y,tar): # each function returns bool, x, y
    acr, i, j = attack_check_rows(tttboard,x,y,tar)
    if acr:
        return True, i, j
    
    acc, i, j = attack_check_columns(tttboard,x,y,tar)
    if acc:
        return True, i, j

    acrd, i, j = attack_check_right_diag(tttboard,x,y,tar)
    if acrd:
        return True, i, j

    acld, i, j = attack_check_left_diag(tttboard,x,y,tar)
    if acld:
        return True, i, j
    
    return False, -1, -1

def attack_check_rows(tttboard,x,y,tar):
    for i in range(y-tar+1,y+1):
        if i < 0 or i > 5:
            continue
        extracted = []
        for j in range(i,i+tar): 
            extracted.append(tttboard[x][j])
        lst, away = test(extracted)
        if lst:
            return True, x, i+away
    return False, -1, -1

def attack_check_columns(tttboard,x,y,tar):
    for i in range(x-tar+1,x+1):
        if i < 0:
            continue
        extracted = []
        for j in range(i,i+tar):
            extracted.append(tttboard[j][y])
        lst, away = test(extracted)
        if lst:
            return True, i+away, y    
    return False, -1, -1

def attack_check_right_diag(tttboard,x,y,tar):
    for i in range(0,tar):
        if x-i > 5 or x-i < 0 or y-i < 0 or y-i > 5:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[x-i+j][y-i+j])
        lst, away = test_wins(extracted)
        if lst:
            return True, x-i+away, y-i+away 
    return False, -1, -1

def attack_check_left_diag(tttboard,x,y,tar):
    n = len(tttboard)
    for i in range(0,tar):
        if x+i >= n or y-i < 0:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[j+x-i][j+y-i])
        lst, away = test(extracted)
        if lst:
            return True, x+i+away, y-i+away
    return False, -1, -1


def check_win_right_diag(tttboard,x,y,tar=5):
    for i in range(0,tar):
        if x+i < 0 or x-i > 5 or y+i < 0 or y+i > 5:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[x+i-j][y-i+j])
        lst, away = test_wins(extracted)
        if lst:
            return True, x-i+away, y-i+away 
    return False, -1, -1
    
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Attack Ends Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Defense Starts Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

def test_def(extracted):

    condi1 = [" ", p1, p1, p1, " "] #4
    condi2 = [" ", p1, p1, " ", p1] #3
    condi3 = [" ", p1, " ", p1, p1] #2

    condi4 = [p1, " ", p1, p1, " "] #2
    condi5 = [p1, " ", p1, " ", p1] #3
    condi6 = [p1, p1, " ", p1, " "] #2

    condi7 = [p1, p1, p1, p1, " "]  #4
    condi8 = [" ", p1, p1, p1, p1]  #0



    if extracted == condi1:
        return True, 4
    elif extracted == condi2 or extracted == condi5:
        return True, 3
    elif extracted == condi3 or extracted == condi4 or extracted == condi6:
        return True, 2
    elif extracted == condi7:
        return True, 4
    elif extracted == condi8:
        return True, 0
    else:
        return False, None

def cpu_defence(tttboard):
    for i in range(len(tttboard)):
        for j in range(len(tttboard[i])):
            if tttboard[i][j] == p1:

                dmr, posx, posy = check_def_row(tttboard, i, j, 5)
                if dmr:
                    return True, posx, posy

                dmc, posx, posy = check_def_column(tttboard, i, j, 5)
                if dmc:
                    return True, posx, posy

                dmrd, posx, posy = check_def_right_diag(tttboard, i, j, 5)
                if dmrd:
                    return True, posx, posy
                
                dmld, posx, posy = check_def_left_diag(tttboard, i, j, 5)
                if dmld:
                    return True, posx, posy

    return False, -1, -1

def check_def_row(tttboard, x, y, tar):
    for i in range(y-tar+1,y+1):
        if i < 0 or i > 5:
            continue
        extracted = []
        for j in range(i,i+tar): 
            extracted.append(tttboard[x][j])
        lst, away = test_def(extracted)
        if lst:
            return True, x, i+away
    return False, -1, -1

def check_def_column(tttboard, x, y, tar):
    for i in range(x-tar+1,x+1):
        if i < 0 or i > 5:
            continue
        extracted = []
        for j in range(i,i+tar):
            extracted.append(tttboard[j][y])
        lst, away = test_def(extracted)
        if lst:
            return True, i+away, y    
    return False, -1, -1

def check_def_right_diag(tttboard,x,y,tar):
    for i in range(0,tar):
        if x-i > 5 or x-i < 0 or y-i < 0 or y-i > 5:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[x-i+j][y-i+j])
        lst, away = test_wins(extracted)
        if lst:
            return True, x-i+away, y-i+away 
    return False, -1, -1

def check_def_left_diag(tttboard, x, y, tar=5):
    for i in range(0,tar):
        if x+i < 0 or x-i > 5 or y+i < 0 or y+i > 5:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[x+i-j][y-i+j])
        lst, away = test_wins(extracted)
        if lst:
            return True, x-i+away, y-i+away 
    return False, -1, -1

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Defence Ends Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Normal Starts Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
def normal_move(tttboard):
    n = len(tttboard)
    optimum = [4,5]
    isoptimum = True
    isnear = True

    while isoptimum == True:
        for i in range(len(optimum)):
            for j in range(len(optimum)):
                if tttboard[optimum[i]][optimum[j]] == " ":
                    return(optimum[i],optimum[j])
                isoptimum = False
                    
                    
    while isnear == True:
        for i in range(n):
            for j in range(n):
                if tttboard[i][j] == "O":
                    if tttboard[i+1][j] == " " :
                        return(i+1,j)
                    elif tttboard[i-1][j] == " ":
                        return(i-1,j)
                    elif tttboard[i][j+1] == " ":
                        return(i,j+1)
                    elif tttboard[i][j-1] == " ":
                        return(i,j-1)
                    elif tttboard[i+1][j+1] == " ":
                        return(i+1,j)  
                    elif tttboard[i-1][j-1] == " ":
                        return(i-1,j-1)
                    isnear = False  

    for i in range(n):
        for j in range(n):
            if tttboard[i][j] == " ":
                return (i,j) #Fills up an empty cell,  Location for CPU isn't used    
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Normal Ends Here~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##

# track each player's data
# keep track of both player and CPU information
# information to store:
#   - every point that is played in
#   - surroundings to know dangerous places ** watch out for same column, row, diag
#   - direction (row,col,etc) and missing cells (to know where to play next time)
#   - not only based on direction, but also groups of five (threshold)
#   - prioritize based on no of items in a group of five
#   - note if the space is less than the threshold
# label for columns, rows, and diagonals - co3, ro4, rd7, ld1
# if the space is less than the threshold, play at the center so that the other player cannot win using that row again
# Player is X, CPU is O

# For CPU, []
# For Player, [ro4: {[4,14,24,34],[44,56,65,75,84]}]
# 
# Data structure
# Each player has a dictionary of groups of five based on number in each group
# So, Player_Dict = {4: {}, 3: {}, 2: {}}
# Each list based on number-in-a-row contains a dictionary pointing directions to groups of five
# Each group of five is an object having a starting point and missing coordinates
# *** Coordinates in this data are stored as 10*x +y not as (x,y) for saving space

class GroupThresh:
    def __init__(self,thresh,char,start):
        self.thresh = thresh
        self.native_char = char
        self.start_pos = start
        self.missing = []
    
    def update_group(self,new_pos):
        self.missing.pop(new_pos)

play_game(10,5)