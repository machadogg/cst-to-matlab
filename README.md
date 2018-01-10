# cst-to-matlab

PYTHON 3!!!

testing script to make a txt file, from CST, readeable on matlab

I am new to programing, and the objective of this project is to convert a text file generated on CST Microwave Studio into a CSV
format that is easily readable on matlab.

Instructions:

1 - Install Python 3, if you don't have it installed yet;
2 - Run 'main.py' script;
3 - Choose the txt file that you want to convert (exported from CST):
    Do not put the extension of your file. The software knows that CST exports TXT (ASCII).
    So, if you exported: cstplot.txt - just type: cstplot

4 - Choose a name for the output file;
5 - Tell the scritp whether your export is from a parameter sweep:
    The script is able to the detect if the plot is from S or Z parameters, or results from a Floqet port,
    but when you make a parameter sweep, the script can't tell the difference between the parameters, so it
    will export the CSV with the original name of your CST export.
    
    Example: if your file is the plot for "SZmax(1),Zmax(1)", it can tell that it is the S11 for the TE mode,
    and it will export it as: s11-te. But, if you have multiple plots, on the same file, from a parameter sweep,
    e.g, "SZmax(1),Zmax(1)_(w=0.05)" and "SZmax(1),Zmax(1)_(w=0.1)", it will export with those names.
    
6 - Use Matlab, or any other software, to import the CSV and plot your graphics.
