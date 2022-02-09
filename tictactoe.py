from math import inf as infinity
from random import choice
import platform
import time
from os import system

Mens = -1
AI = +1
Speelveld = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def game_over(state):

    return WinCheck(state, Mens) or WinCheck(state, AI)

def Leeg_hokje(state):

    Hokjes = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                Hokjes.append([x, y])

    return Hokjes

def Maak_Zet(x, y, speler):

    if ZetChecker(x, y):
        Speelveld[x][y] = speler
        return True
    else:
        return False

def ZetChecker(x, y):

    if [x, y] in Leeg_hokje(Speelveld):
        return True
    else:
        return False

def MaakSchermSchoon():

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def PrintScherm(state, AI_Keuze, Mens_Keuze):

    chars = {
        -1: Mens_Keuze,
        +1: AI_Keuze,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def AI_Zet(AI_Keuze, Mens_Keuze):
    Diepte = len(Leeg_hokje(Speelveld))
    if Diepte == 0 or game_over(Speelveld):
        return

    MaakSchermSchoon()
    print(f'AIuter turn [{AI_Keuze}]')
    PrintScherm(Speelveld, AI_Keuze, Mens_Keuze)

    if Diepte == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        Zetnr = minimax(Speelveld, Diepte, AI)
        x, y = Zetnr[0], Zetnr[1]

    Maak_Zet(x, y, AI)

def WinCheck(state, speler):

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [speler, speler, speler] in win_state:
        return True
    else:
        return False

def minimax(state, Diepte, speler):

    if speler == AI:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if Diepte == 0 or game_over(state):
        score = CheckWin(state)
        return [-1, -1, score]

    for cell in Leeg_hokje(state):
        x, y = cell[0], cell[1]
        state[x][y] = speler
        score = minimax(state, Diepte - 1, -speler)
        state[x][y] = 0
        score[0], score[1] = x, y

        if speler == AI:
            if score[2] > best[2]:
                best = score 
        else:
            if score[2] < best[2]:
                best = score 

    return best

def CheckWin(state):
    if WinCheck(state, AI):
        score = +1
    elif WinCheck(state, Mens):
        score = -1
    else:
        score = 0

    return score

def main():
    MaakSchermSchoon()
    Mens_Keuze = '' 
    AI_Keuze = ''  
    EersteZet = ''  


    while Mens_Keuze != 'O' and Mens_Keuze != 'X':
        try:
            print('')
            Mens_Keuze = input('Kies X of O\nGekozen: ').upper()
        except (EOFError, KeySpeelveldInterrupt):
            print('Doei')
            exit()
        except (KeyError, ValueError):
            print('Deze zet mag niet')


    if Mens_Keuze == 'X':
        AI_Keuze = 'O'
    else:
        AI_Keuze = 'X'

 
    MaakSchermSchoon()
    while EersteZet != 'Y' and EersteZet != 'N':
        try:
            EersteZet = input('Wilt u beginnen[y/n]?: ').upper()
        except (EOFError, KeySpeelveldInterrupt):
            print('Doei')
            exit()
        except (KeyError, ValueError):
            print('Deze zet mag niet')

    while len(Leeg_hokje(Speelveld)) > 0 and not game_over(Speelveld):
        if EersteZet == 'N':
            AI_Zet(AI_Keuze, Mens_Keuze)
            EersteZet = ''

        Mens_Zet(AI_Keuze, Mens_Keuze)
        AI_Zet(AI_Keuze, Mens_Keuze)


    if WinCheck(Speelveld, Mens):
        MaakSchermSchoon()
        print(f'Mens zet [{Mens_Keuze}]')
        PrintScherm(Speelveld, AI_Keuze, Mens_Keuze)
        print('Jij wint!')
    elif WinCheck(Speelveld, AI):
        MaakSchermSchoon()
        print(f'AI aan de beurt [{AI_Keuze}]')
        PrintScherm(Speelveld, AI_Keuze, Mens_Keuze)
        print('Jij verliest!')
    else:
        MaakSchermSchoon()
        PrintScherm(Speelveld, AI_Keuze, Mens_Keuze)
        print('Gelijk spel')

    #exit()
    
def Mens_Zet(AI_Keuze, Mens_Keuze):

    Diepte = len(Leeg_hokje(Speelveld))
    if Diepte == 0 or game_over(Speelveld):
        return


    Zetnr = -1
    WinMogelijkheid = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    #MaakSchermSchoon()
    print(f'Mens turn [{Mens_Keuze}]')
    PrintScherm(Speelveld, AI_Keuze, Mens_Keuze)

    while Zetnr < 1 or Zetnr > 9:
        try:
            Zetnr = int(input('Use numpad (1..9): '))
            coord = WinMogelijkheid[Zetnr]
            can_Zetnr = Maak_Zet(coord[0], coord[1], Mens)

            if not can_Zetnr:
                print('Bad Zetnr')
                Zetnr = -1
        except (EOFError, KeySpeelveldInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


if __name__ == '__main__': 
    main()