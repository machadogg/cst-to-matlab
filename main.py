from functions import *
import re

with open("test2.txt", 'r') as rf:

    text = rf.read()
    liss = re.split("\n", text)

    liss = del_dashes(liss)
    printdeb()
    liss = define_Sparam(liss)

    adjusting(liss)

    with open("write.txt", "w") as wf:

        for item in liss:
            wf.write(item + '\n')
