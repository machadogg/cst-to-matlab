from functions import *
import re
import os

rfn = input("Enter the name for the file to be converted (without extension): ")
wfw = input("Enter the output file name (without extension): ")

rfn = rfn + '.txt'
wfw = wfw + '.csv'

try:
    with open(rfn, 'r') as rf:

        text = rf.read()
        liss = re.split("\n", text)

        liss = del_dashes(liss)
        # printdeb()
        liss = define_Sparam(liss)

        with open(wfw, "w") as wf:

            for item in liss:
                wf.write(item + '\n')
        print(rfn + ' converted successfuly \n\n')

except EnvironmentError:
    print("\n\nError opening the file. Does it exist? \nRemember: DO NOT write the file extension \nexemple: test, and not 'text.txt'\n\n")


os.system('pause')
