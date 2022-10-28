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
    tttboard = [] # this keeps record of the board, either X or O or " "
    plays = 0 # number of time both players have played in total

    # generate a double array of spaces as an initial board
    inner = []
    for i in range(0,n):
        inner.append(" ")
    for i in range(0,n):
        tttboard.append(inner[:])
      
    # To check if someone has won. If anyone wins, won is going to be
    # a  string: X wins, O wins, or DRAW
    won = None

    CPU = True
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
            ava_location = CPU_next_move(tttboard)  #ava_location = avaiableLocation for CPU moves
            x = ava_location[0]
            y = ava_location[1]

        # the current player has to choose a location to play to

        if curr_player:
            tttboard[x][y] = "X"
            if check_win(tttboard, x, y, thresh, "X"): # check if X has won
                draw_board(tttboard)
                won = "X wins" # won is no longer None. While loop breaks
                continue
        else:
            tttboard[x][y] = "O"
            if check_win(tttboard, x, y, thresh, "O"): # check if Y has won
                draw_board(tttboard)
                won = "O wins" # won is no longer None. While loop breaks
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
    global curr_player
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
    global curr_player
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
    global curr_player
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
    global curr_player
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

def CPU_next_move(tttboard): #Telling CPU where it can make a move/play
    n = len(tttboard)
    for i in range(n):
        for j in range(n):
            if tttboard[i][j] == " ":
                return (i,j) #Fills up an empty cell,  Location for CPU isn't used

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