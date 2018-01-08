from functions import *
import re

rfn = input("Enter the name for the file to be converted: ")
wfw = input("Enter the output file name: ")

with open("test4.txt", 'r') as rf:

    text = rf.read()
    liss = re.split("\n", text)

    liss = del_dashes(liss)
    printdeb()
    liss = define_Sparam(liss)

    with open("write3.csv", "w") as wf:

        for item in liss:
            wf.write(item + '\n')

print(len(liss))
