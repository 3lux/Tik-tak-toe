import PySimpleGUI as sg
fl = ['-', '-', '-']
sl = ['-', '-', '-']
tl = ['-', '-', '-']
flstr =' '.join(fl)
slstr =' '.join(sl)
tlstr =' '.join(tl)
sg.theme('BlueMono')
turn=0
def update_fl():
    try:
        window['first'].update(flstr)
    except:
        window['first'].update(flstr)
def update_sl():
    try:
        window['second'].update(slstr)
    except:
        window['second'].update(slstr)
def update_tl():
    try:
        window['third'].update(tlstr)
    except:
        window['third'].update(tlstr)
bs = {'size':(8,2), 'button_color':()}

layout = [  [sg.Text(flstr, size=(50,1), font=(24), justification='center', key='first')],
            [sg.Text(slstr, size=(50,1), font=(24), justification='center', key='second')],
            [sg.Text(tlstr, size=(50,1), font=(24), justification='center', key='third')],
            [sg.Button('',key = '1', **bs), sg.Button('',key = '2',**bs), sg.Button('',key = '3',**bs)],
            [sg.Button('',key = '4',**bs), sg.Button('',key = '5',**bs), sg.Button('',key = '6',**bs)],
            [sg.Button('',key = '7',**bs), sg.Button('',key = '8',**bs), sg.Button('',key = '9',**bs)]]


window = sg.Window('Tic-Tac-Toe', layout=layout, size =(300,400))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    if event == '1' and turn==0:
        fl[0]= 'x'
        flstr =' '.join(fl)
        update_fl()
    if event == '2' and turn==0:
        fl[1]= 'x'
        flstr =' '.join(fl)
        update_fl()
    if event == '3' and turn==0:
        fl[2]= 'x'
        flstr =' '.join(fl)
        update_fl()
    if event == '4' and turn==0:
        sl[0] = 'x'
        slstr =' '.join(sl)
        update_sl()
    if event == '5' and turn==0:
        sl[1] = 'x'
        slstr =' '.join(sl)
        update_sl()
    if event == '6' and turn==0:
        sl[2] = 'x'
        slstr =' '.join(sl)
        update_sl()
    if event == '7' and turn==0:
        tl[0]= 'x'
        tlstr =' '.join(tl)
        update_tl()
    if event == '8' and turn==0:
        tl[1]= 'x'
        tlstr =' '.join(tl)
        update_tl()
    if event == '9' and turn==0:
        tl[2]= 'x'
        tlstr =' '.join(tl)
        update_tl()
window.close()
