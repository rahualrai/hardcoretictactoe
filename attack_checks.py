CPU = "X"
p1 = "O"


def test(extracted):
    global condi1, condi2, condi3

    condi1 = [" ", CPU, CPU, CPU, " "]
    condi2 = [" ", CPU, " ", CPU, CPU]
    condi3 = [CPU, " ", CPU, CPU, " "]

    if extracted == condi1:
        return True, 0
    elif extracted == condi2:
        return True, 2
    elif extracted == condi3:
        return True,1


def check_attack(tttboard,x,y,tar,ch): # each function returns bool, x, y
      if attack_check_rows(tttboard,x,y,tar,ch):
        return True
      elif attack_check_columns(tttboard,x,y,tar,ch):
        return True
      elif attack_check_right_diag(tttboard,x,y,tar,ch):
        return True
      elif attack_check_left_diag(tttboard,x,y,tar,ch):
        return True
      else: 
        return False

def attack_check_rows(tttboard,x,y,tar,ch): #ch = X
    global curr_player
    for i in range(y-tar+1,y+1):
        if i < 0 or i > 5:
            continue
        extracted = []
        for j in range(i,i+tar): 
            extracted.append(tttboard[x][j])
        if test(extracted)[0]:
            away = test(extracted)[1]
            return True, x, i+away            

  
def attack_check_columns(tttboard,x,y,tar,ch):
    global curr_player
    for i in range(x-tar+1,x+1):
        if i < 0:
            continue
        extracted = []
        for j in range(i,i+tar):
            extracted.append(tttboard[j][y])
        if test(extracted)[0]:
            away = test(extracted)[1]
            return True, i+away, y            


def attack_check_right_diag(tttboard,x,y,tar,ch):
    global curr_player
    n = len(tttboard)
    for i in range(0,tar):
        if x-i < 0 or y-i < 0:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[j+x-i][j+y-i])
        if test(extracted)[0]:
            away = test(extracted)[1]
            return True, x-i+away, y-i+away 

def attack_check_left_diag(tttboard,x,y,tar,ch):
    global curr_player
    n = len(tttboard)
    for i in range(0,tar):
        if x+i >= n or y-i < 0:
            continue
        extracted = []
        for j in range(0,tar):
            extracted.append(tttboard[j+x-i][j+y-i])
        if test(extracted)[0]:
            away = test(extracted)[1]
            return True, x+i+away, y-i+away