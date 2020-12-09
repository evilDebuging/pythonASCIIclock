import os, time
from time import localtime, strftime

'''
ASCII art numbers
'''
_0='  ______  \n /      \ \n|  ▓▓▓▓▓▓\ \n| ▓▓▓\| ▓▓\n| ▓▓▓▓\ ▓▓\n| ▓▓\▓▓\▓▓\n| ▓▓_\▓▓▓▓\n \▓▓  \▓▓▓\n  \▓▓▓▓▓▓ '
_1='\n   __   \n _/  \  \n|   ▓▓  \n \▓▓▓▓  \n  | ▓▓  \n  | ▓▓  \n _| ▓▓_ \n|   ▓▓ \ \n \▓▓▓▓▓▓'
_2='\n  ______   \n /      \  \n|  ▓▓▓▓▓▓\ \n \▓▓__| ▓▓ \n /      ▓▓ \n|  ▓▓▓▓▓▓  \n| ▓▓_____  \n| ▓▓     \ \n \▓▓▓▓▓▓▓▓ \n'
_3='  ______   \n /      \  \n|  ▓▓▓▓▓▓\ \n \▓▓__| ▓▓ \n  |     ▓▓ \n __\▓▓▓▓▓\ \n|  \__| ▓▓ \n \▓▓    ▓▓ \n  \▓▓▓▓▓▓'
_4='\n __    __ \n|  \  |  \ \n| ▓▓  | ▓▓\n| ▓▓__| ▓▓\n| ▓▓    ▓▓\n \▓▓▓▓▓▓▓▓\n      | ▓▓\n      | ▓▓\n       \▓▓'
_5='\n _______ \n|       \ \n| ▓▓▓▓▓▓▓\n| ▓▓____ \n| ▓▓    \ \n \▓▓▓▓▓▓▓\ \n|  \__| ▓▓\n \▓▓    ▓▓\n  \▓▓▓▓▓▓ '
_6='\n  ______  \n /      \ \n|  ▓▓▓▓▓▓\ \n| ▓▓___\▓▓\n| ▓▓    \ \n| ▓▓▓▓▓▓▓\ \n| ▓▓__/ ▓▓\n \▓▓    ▓▓\n  \▓▓▓▓▓▓ '
_7='\n ________ \n|        \ \n \▓▓▓▓▓▓▓▓\n    /  ▓▓ \n   /  ▓▓  \n  /  ▓▓   \n /  ▓▓    \n|  ▓▓    \n \▓▓     '
_8='\n  ______  \n /      \ \n|  ▓▓▓▓▓▓\ \n| ▓▓__/ ▓▓\n >▓▓    ▓▓\n|  ▓▓▓▓▓▓ \n| ▓▓__/ ▓▓\n \▓▓    ▓▓\n  \▓▓▓▓▓▓ '
_9='\n  ______  \n /      \ \n|  ▓▓▓▓▓▓\ \n| ▓▓__/ ▓▓\n \▓▓    ▓▓\n _\▓▓▓▓▓▓▓\n|  \__/ ▓▓\n \▓▓    ▓▓\n  \▓▓▓▓▓▓ '
listNumber=[_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]

def timeSplitter(time):
    x=y=0# x is the position of the number (0 or 1), y the number to test
    h, m, s=strftime('%H'), strftime('%M'), strftime('%S')#Local time using time library
    listHour, listMinute, listSecond=list(h), list(m), list(s)#split the numbers

    for i in range(2):
        for i in range(10):
            if str(y)==time[x]:
                if x==0:
                    print(listNumber[y])
                elif x==1:
                    print(listNumber[y], '\n \n')
                break
            y=y+1
        x=x+1
        y=0

while True:
    os.system('cls')

    h, m, s=strftime('%H'), strftime('%M'), strftime('%S')
    listHour, listMinute, listSecond=list(h), list(m), list(s)

    timeSplitter(listHour)
    timeSplitter(listMinute)
    timeSplitter(listSecond)
    print(strftime("%Y-%m-%d", localtime()))

    time.sleep(1)#final value=1
