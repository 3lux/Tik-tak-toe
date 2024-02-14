import random
fl = ['-', '-', '-', '-',
'-', '-', '-',
'-', '-', '-']
available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_moves = []
ai_moves = []
lpl = []
lcl = []
def reset():
    fl = ['-', '-', '-', '-',
'-', '-', '-',
'-', '-', '-']
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lp = ''
    lc = ''
    return fl, available, lp, lc 

def choice(fl=fl):
   
    print("choose ‘x’ or ‘o’")
    while True:
        try:
            lp = input()
            if lp in ['x', 'o']:
                if lp == 'x':
                    lpl.append('x')
                    lcl.append('o')
                    break
                else:
                    lpl.append('o')
                    lcl.append('x')
                    break
            else:
                print('type x/o')
                continue
            
        except:
            print('type x/o')
            continue
    print("you chose "+lp)
    print("you're up against "+lcl[0])
    return fl, lpl, lcl

def print_board(fl=fl):
    print(fl[1], fl[2], fl[3])
    print(fl[4], fl[5], fl[6])
    print(fl[7], fl[8], fl[9])
    
def move(fl=fl, lpl=lpl, lcl=lcl):
    print('your turn, choose a position: 1-9')
    while True:
        try:
            i = int(input())
            if i in available:
                fl[i] = lpl[0]
                print('you chose '+str(i))
                available.remove(i)
                player_moves.append(i)
                break
            else:
                print(str(i)+' is already taken')
        except: 
            print('type numbers 1-9')
            continue
    return fl
def bot_random(fl=fl, lpl=lpl, lcl=lcl):
    while True:
        bot = random.randint(1, 9)
        if bot in available:
            fl[bot] = lcl[0]
            available.remove(bot)
            ai_moves.append(bot)
            break
        else:
            continue
        
    print('your enemy chose '+str(bot))
    return fl

def winning_move(le, moves, fl=fl, available=available):
            #1
            if all(x in moves for x in [1,2]) and 3 in available:
                fl[3] = le[0]
                available.remove(3)
                ai_moves.append(3)
                return True, fl
            elif all(x in moves for x in [1,3]) and 2 in available:
                fl[2] = le[0]
                available.remove(2)
                ai_moves.append(2)
                return True, fl
            elif all(x in moves for x in [2,3]) and 1 in available:
                fl[1] = le[0]
                available.remove(1)
                ai_moves.append(1)
                return True, fl
            #2
            elif all(x in moves for x in [5,6]) and 4 in available:
                fl[4] = le[0]
                available.remove(4)
                ai_moves.append(4)
                return True, fl
            elif all(x in moves for x in [4,6]) and 5 in available:
                fl[5] = le[0]
                available.remove(5)
                ai_moves.append(5)
                return True, fl
            elif all(x in moves for x in [4,5]) and 6 in available:
                fl[6] = le[0]
                available.remove(6)
                ai_moves.append(6)
                return True, fl
            #3
            elif all(x in moves for x in [8,9]) and 7 in available:
                fl[7] = le[0]
                available.remove(7)
                ai_moves.append(7)
                return True, fl
            elif all(x in moves for x in [7,9]) and 8 in available:
                fl[8] = le[0]
                available.remove(8)
                ai_moves.append(8)
                return True, fl
            elif all(x in moves for x in [7,7]) and 9 in available:
                fl[9] = le[0]
                available.remove(9)
                ai_moves.append(9)
                return True, fl
            #4
            elif all(x in moves for x in [1,4]) and 7 in available:
                fl[7] = le[0]
                available.remove(7)
                ai_moves.append(7)
                return True, fl
            elif all(x in moves for x in [1,7]) and 4 in available:
                fl[4] = le[0]
                available.remove(4)
                ai_moves.append(4)
                return True, fl
            elif all(x in moves for x in [4,7]) and 1 in available:
                fl[1] = le[0]
                available.remove(1)
                ai_moves.append(1)
                return True, fl
            #5
            elif all(x in moves for x in [2,5]) and 8 in available:
                fl[8] = le[0]
                available.remove(8)
                ai_moves.append(8)
                return True, fl
            elif all(x in moves for x in [2,8]) and 5 in available:
                fl[5] = le[0]
                available.remove(5)
                ai_moves.append(5)
                return True, fl
            elif all(x in moves for x in [5,8]) and 2 in available:
                fl[2] = le[0]
                available.remove(2)
                ai_moves.append(2)
                return True, fl
            #6
            elif all(x in moves for x in [3,6]) and 9 in available:
                fl[9] = le[0]
                available.remove(9)
                ai_moves.append(9)
                return True, fl
            elif all(x in moves for x in [3,9]) and 6 in available:
                fl[6] = le[0]
                available.remove(6)
                ai_moves.append(6)
                return True, fl
            elif all(x in moves for x in [6,9]) and 3 in available:
                fl[3] = le[0]
                available.remove(3)
                ai_moves.append(3)
                return True, fl
            #7
            if all(x in moves for x in [1,5]) and 9 in available:
                fl[9] = le[0]
                available.remove(9)
                ai_moves.append(9)
                return True, fl
            elif all(x in moves for x in [1,9]) and 5 in available:
                fl[5] = le[0]
                available.remove(5)
                ai_moves.append(5)
                return True, fl
            elif all(x in moves for x in [5,9]) and 1 in available:
                fl[1] = le[0]
                available.remove(1)
                ai_moves.append(1)
                return True, fl
            #8
            elif all(x in moves for x in [3,5]) and 7 in available:
                fl[7] = le[0]
                available.remove(7)
                ai_moves.append(7)
                return True, fl
            elif all(x in moves for x in [3,7]) and 5 in available:
                fl[5] = le[0]
                available.remove(5)
                ai_moves.append(5)
                return True, fl
            elif all(x in moves for x in [5,7]) and 3 in available:
                fl[3] = le[0]
                available.remove(3)
                ai_moves.append(3)
                return True, fl
            else:
                return False
def ai_move(le=lcl, moves=ai_moves, fl=fl, available=available):
    winning_move(lcl, ai_moves)
    if winning_move(lcl, ai_moves) == False:
        winning_move(lcl, player_moves)
        if winning_move(lcl, player_moves) == False:
                if all(x in available for x in [1,3,7,9]): 
                    while True:
                        bot = random.randint(1, 9)
                        if bot in [1,3,7,9]:
                            fl[bot] = lcl[0]
                            available.remove(bot)
                            ai_moves.append(bot)
                            break
                        else:
                            continue
            
                elif 5 in available:
                    fl[5] = lcl[0]
                else:
                    while True:
                        bot = random.randint(1, 9)
                        if bot in available:
                            fl[bot] = lcl[0]
                            available.remove(bot)
                            ai_moves.append(bot)
                            break
                        else:
                            continue
    
    return fl

while True:
    reset()
    choice()
    print_board()
    
    move()
    bot_random()
    print_board()
    
    move()
    ai_move()
    print_board()

    move()
    ai_move()
    print_board()

    move()
    ai_move()
    print_board()

    move()
    print_board()
    #print_board()
    #move()
    #bot_random()
    #print_board()
    #move()
    #bot_random()
    #print_board()
    print('play again? y/n')
    repeat = input()
    if repeat == 'y':
        continue
    else:
        quit()
