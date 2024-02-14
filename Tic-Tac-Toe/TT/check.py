letter = 'x'
letter_opposite = 'o'
fl = ['x', 'x', '-',
      'o', '-', '-',
      'o', '-', '-']
def indices(element, lst = fl):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def check_player(letter = letter, letter_opposite = letter_opposite, fl=fl):
    total = len(indices(letter))
    i = 0
    a = -1
    while a > -total:
        if i == total-1:
            break
        if a == -total+1:
            a=0
            i+=1
        if abs(indices(letter)[i]-indices(letter)[a]) in [1, 3, 4]:
            align = abs(indices(letter)[i]-indices(letter)[a])
            if indices(letter)[i] == 0:
                pass
        
            if indices(letter)[i] in [2, 5, 8, 7, 6]:
                pass
        
    
    return
check_player()
