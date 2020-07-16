import argparse
import posixpath
import csv
from io import *
import os
import numpy as np

ALL_STRINGS = []
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# PARSER INTRO
parser = argparse.ArgumentParser(
    description="Set the index of each formula"
)
parser.add_argument("file", type=str, action="store")
args = parser.parse_args()
file = posixpath.join(*args.file.split("\\"))
name_file = file.upper()
file = f"FORMULAS/TXT/{file}.txt"

#folder,subfolder = file.split("/")

formula_file = open(f"{file}","r")
formula_file = formula_file.readlines()

# print(formula_file)

print("-----------------------------")
#-----------------
print("Select the formula to create the svg\n")
print('\n'.join('{}: {}'.format(*k) for k in enumerate(formula_file,start=1)))
print("-----------------------------")
formula = input("Formula: ")
formula_selected = formula_file[int(formula)-1]
# CLEAN
clean_screen()
ALL_STRINGS = [
    f"\nFormula selected: \n",
    f"    {formula_selected}\n"
]

INDEX = []
count = 0;
while count < len(formula_selected):
    s = formula_selected[count]
    if s not in [" ","\n"]:
        clean_screen()
        print(ALL_STRINGS[0])
        spaces = " "*count
        for pre_write in INDEX:
            print(f"\t\t{pre_write[0]}\t|| {pre_write[1]}")
        print(f"    {spaces}|")
        print(f"    {spaces}v")
        print(ALL_STRINGS[1])
        input_string = input(f"\t\t{count+1})\t{s} || ")
        if input_string.isnumeric():
            pair_append = (s,input_string)
            INDEX.append(pair_append)
        elif s == "\\":
            tex_symbol, *tex_indexes = input_string.split()
            more_spaces = len(tex_symbol)
            sub_count = 1
            for ti in tex_indexes:
                if len(tex_indexes) == 1:
                    pair_append = (tex_symbol,ti)
                    INDEX.append(pair_append)
                else:
                    pair_append = (f"{tex_symbol}_{sub_count}",ti)
                    INDEX.append(pair_append)
                sub_count += 1
            count += more_spaces
    count += 1

print("The indexes are:")
for s,i in INDEX:
    print(f"\t{s} \t|| {i}")

print(f"Finshed formula {formula}")

INDEX = np.array(INDEX)
INDEX_TRANSPOSE = np.transpose(INDEX)

#print(INDEX_TRANSPOSE)
CSV_DIR = f"FORMULAS/{name_file}/CSV"
if not os.path.exists(CSV_DIR):
    os.makedirs(CSV_DIR)

np.savetxt(
    f"{CSV_DIR}/csv_{formula}.csv",
    INDEX_TRANSPOSE,
    delimiter=",",
    fmt='%s'
)