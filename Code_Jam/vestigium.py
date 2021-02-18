#To run this in terminal you need to run

# $ python3 vestigium.py < vestigium.txt

# the < symbol will pass everything from the text file as standard input

import sys
import numpy as np

def unique_list(row):
    unique_list = []
    for x in row:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def checkforrepeats(mat):
    ##We are only checking for rows since process
    ##will send this routine the transpose
    [row,col] = np.shape(mat)
    reps = 0
    for r in range(0,row):
        this_row = mat[r]
        unique = unique_list(this_row)
        if len(unique) != len(this_row):
            reps+=1
    return reps
    
    
def process(mat):
    k = int(np.trace(mat))
    ##First check rows
    r = checkforrepeats(mat)
    #Then check columns
    c = checkforrepeats(np.transpose(mat))
    return k,r,c

everything = sys.stdin.readlines()
ctr = 0
numcases = int(everything[ctr])
ctr+=1
#print('Numcases = ',numcases)

###Loop through cases
for n in range(0,numcases):
    #print('Case ',n+1)

    ###Get Size of Matrix
    sizeofmatrix = int(everything[ctr])
    ctr+=1
    #print('Size of Matrix = ',sizeofmatrix)

    ###Grab Matrix
    mat = []
    for m in range(0,sizeofmatrix):
        row = everything[ctr]
        strs = row.split()
        ints = [int(s) for s in strs]
        ctr+=1
        mat.append(ints)

    ##Process matrix
    mat = np.asarray(mat)
    #print('Matrix = ',mat)
    k,r,c = process(mat)

    print('Case #'+str(n+1)+': '+str(k)+' '+str(r)+' '+str(c))
        
#print('Program Quit')
