#This program makes new files for you

import tkinter #Imports modules
from tkinter import filedialog
from time import strftime


def diropen():
    '''Tkinter select file'''
    fullpath = filedialog.askdirectory(initialdir = "c:\ ",title = "Select Folder")
    root.destroy()
    return fullpath
root = tkinter.Tk()

fpath = diropen()
fpath = fpath + '/'
print(fpath)



def head(fpath):
    '''Makes the header'''
    def space(aft):
        sp = ''
        while len(sp) <= aft:
            sp += ' '
        return sp

    def pound(aft):
        pou = ''
        while len(pou) <= aft:
            pou += '#'
        return pou

    name = input("What is your name? ")

    date = strftime('%b %Y')

    print("Example: \nEx01-01\n^^^^\nLesson")

    les = input('What is the name of the lesson? ')

    print("Does it use a '-' or a '_'?")
    print("1. -")
    print("2. _")
    dash = input(": ")
    if dash == '1':
        dash = '-'
    elif dash == '2':
        dash = '_'
    else:
        print("Dash is -")
        dash = "-"

    start = input("Start at what number? (Press Enter to start at 1) ")
    if start == '':
        x = 0
    else:
        x = start - 1
    
    leslen = len(les)
    while True:
        x += 1

        if x < 10:
            x = str(x)
            x = '0'+x
        x = str(x)

        les = les[:leslen]+dash+x

        lespath = fpath + les + '.py'
        
        
        header  = pound(20)+ '\n'
        header += '#'+name + space(18 - len(name)) + '#\n'
        header += '#'+date + space(18 - len(date)) + '#\n'
        header += '#'+les + space(18 - len(les)) + '#\n'
        header += pound(20) + '\n\n'
        
        header = str(header)
        
        f = open(lespath, 'w')
        f.write(header)
        f.close()

        x = int(x)
        input("Press Enter to make next file")

head(fpath)

