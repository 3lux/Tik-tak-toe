import PySimpleGUI as sg
from random import randint
import time

fl = ['-', '-', '-',
      '-', '-', '-',
      '-', '-', '-']
flstr =' '.join(fl)
sg.theme('BlueMono')
turn=0
first_button = ''
second_button= ''
third_button= ''
fourth_button= ''
fifth_button= ''
sixth_button= ''
seventh_button= ''
eighth_button= ''
ninth_button= ''
def indices(element, lst = fl):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)
        
def update_fl():
    window['first'].update(flstr)
    window['1'].update(first_button)
    window['2'].update(second_button)
    window['3'].update(third_button)
    window['4'].update(fourth_button)
    window['5'].update(fifth_button)
    window['6'].update(sixth_button)
    window['7'].update(seventh_button)
    window['8'].update(eighth_button)
    window['9'].update(ninth_button)

event, values = sg.Window('Choose a letter', [[sg.Listbox(['x','o'], size=(10,3))],  [sg.OK()]]).read(close=True)
if event == 'OK':
    print('You chose', values[0][0])

bs = {'size':(8,2), 'button_color':()}
letter = str(values[0][0])

if letter == 'x':
    letter_opposite = 'o'
else:
    letter_opposite = 'x'



def check_player(letter = letter, letter_opposite = letter_opposite, fl=fl):
    total = len(indices(letter))
    i = 0
    while i < total:
        while a < len:
        if abs(indices(letter)[i]-indices(letter)[i+a]) in [1, 3, 4]:
            align = abs(indices(letter)[i]-indices(letter)[i+a])
            fl[indices(letter)[i] - align] = letter_opposite
            if indices(letter)[i] in [2, 5, 8, 7, 6]:

        else:
            i +=1

#def check_win(turn=turn, letter = letter, letter_opposite = letter_opposite):
    #check = all(item in indices(letter) for item in [0,1,2])
    #if check:
        #print('you win')
        
layout = [  [sg.Text(flstr, size=(4,4), font=(24), justification='center', key='first')],
            [sg.Button(first_button,key = '1', **bs), sg.Button(second_button,key = '2',**bs), sg.Button(third_button,key = '3',**bs)],
            [sg.Button(fourth_button,key = '4',**bs), sg.Button(fifth_button,key = '5',**bs), sg.Button(sixth_button,key = '6',**bs)],
            [sg.Button(seventh_button,key = '7',**bs), sg.Button(eighth_button,key = '8',**bs), sg.Button(ninth_button,key = '9',**bs)],
            [sg.Button('Update',key = 'upd',**bs), sg.Button('Reset',key = 'res',**bs)]]


window = sg.Window('Tic-Tac-Toe', layout=layout, size =(300,400))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    if event == 'upd':
        flstr =' '.join(fl)
        update_fl()
    if event == 'res':
        fl=['-', '-', '-', '-', '-', '-', '-', '-', '-']
        window['1'].update(disabled=False)
        window['2'].update(disabled=False)
        window['3'].update(disabled=False)
        window['4'].update(disabled=False)
        window['6'].update(disabled=False)
        window['5'].update(disabled=False)
        window['7'].update(disabled=False)
        window['8'].update(disabled=False)
        window['9'].update(disabled=False)
        turn = 0
        first_button = ''
        second_button= ''
        third_button= ''
        fourth_button= ''
        fifth_button= ''
        sixth_button= ''
        seventh_button= ''
        eighth_button= ''
        ninth_button= ''
    if event == '1':
            fl[0]= letter
            turn +=1
            window['1'].update(disabled=True)
            first_button = letter
    if event == '2':
            fl[1]= letter 
            turn +=1
            window['2'].update(disabled=True)
            second_button = letter
    if event == '3':
            fl[2]= letter
            turn +=1
            window['3'].update(disabled=True)
            third_button= letter

    if event == '4':
            fl[3] = letter
            turn +=1
            window['4'].update(disabled=True)
            fourth_button= letter

    if event == '5':
            fl[4] = letter
            turn +=1
            window['5'].update(disabled=True)
            fifth_button= letter

    if event == '6':
            fl[5] = letter
            turn +=1
            window['6'].update(disabled=True)
            sixth_button= letter

    if event == '7':
            fl[6]= letter
            turn +=1
            window['7'].update(disabled=True)
            seventh_button= letter

    if event == '8':
            fl[7]= letter
            turn +=1
            window['8'].update(disabled=True)
            eighth_button= letter

    if event == '9':
            fl[8]= letter
            turn +=1
            window['9'].update(disabled=True)
            ninth_button= letter
    if letter == 'o':
        bot = randint(0,8)
        fl[bot] = letter_opposite
    if turn == 1 and letter == 'x':
        bot = randint(0,8)
        if fl[bot] != letter_opposite and fl[bot] != letter:
            fl[bot] = letter_opposite
            window[str(bot+1)].update(disabled=True)
        else:
            bot = randint(0,bot)
            fl[bot] = letter_opposite
    if turn ==2:
        check_player()
    if turn ==3:
        check_player()
    if turn ==4:
        check_player()
    if turn ==5:
        check_player()  
            
    print(turn)
    #print(indices('o'), turn)
    flstr =' '.join(fl)
    update_fl()
window.close()
