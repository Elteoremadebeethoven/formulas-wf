import csv
from io import *
import os
import numpy as np
import posixpath
import argparse

parser = argparse.ArgumentParser(
    description="Set the index of each formula"
)
parser.add_argument("file", type=str, action="store")
args = parser.parse_args()
file = posixpath.join(*args.file.split("\\"))
name_file = file.upper()
file = f"FORMULAS/TXT/{file}.txt"

formula_file = open(f"{file}","r")
formula_file = formula_file.readlines()
csv_range = len(formula_file)

def rango(n):
    return range(n+1)
def add_quote(row):
    new_row=[]
    for r in row:
        r+=','
        new_row.append(r)
    return new_row
def es_par(n):
    if n%2==0:
        return True
    else:
        return False


rows=[]
list_0=list(range(1,csv_range+1))
list_1=list_0.copy()

list_1.append(csv_range)
list_1.pop(0)

for f_i,f_f in zip(list_0,list_1):
    for string in range(f_i,f_f+1):
        pre_rows=[]
        with open(f"FORMULAS/{name_file}/CSV"+'/%s_%s.csv'%("csv",string), 'r') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                pre_rows.append(row)
            if string==f_i:
                rows.append(['Step: %s'%(f_i)])
                rows.append(['\t']+['N']+add_quote(pre_rows[1])+['),'])
                rows.append(['\t']+['[%s]'%f_i]+pre_rows[0])
            else:
                rows.append(['\t']+['[%s]'%f_f]+pre_rows[0])
                rows.append(['\t']+['N']+add_quote(pre_rows[1])+[')'])
                rows.append("\n")
                rows.append(['pre_fade:']+['('])
                rows.append(['pre_copy:']+['('])
                rows.append("\n")
                rows.append(['*run_fade:']+['('])
                rows.append(['>pre_form:']+['('])
                rows.append(['>pos_form:']+['('])
                rows.append(['*run_write:']+['('])
                rows.append("\n")
                rows.append(['pos_copy:']+['('])
                rows.append(['pos_write:']+['('])
                rows.append("\n")
                rows.append("\n")
                rows.append(['---------']*50)
                rows.append("\n")




with open(f"FORMULAS/{name_file}/CSV"+'/all_csv.csv','w',newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [
                *rows
            ]
    a.writerows(data)
