from time import strftime

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

name = raw(input("What is your name? "))

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

    print(pound(20))
    print('#'+name, space(16 - len(name)), '#')
    print('#'+date, space(16 - len(date)), '#')
    print('#'+les, space(16 - len(les)), '#')
    print(pound(20))

    x = int(x)
    input()
