import os
import os.path
import string
from os.path import join
 
PRINTPATH = False
 
def calDiff(oldFile, newFile, fileName):
    commLen = []
    oldLines = 0
    newLines = 0
    newContents = []
    oldContents = []
    minDiffs = []
# minDiffs[[[a, b, c, d, e, f],...],...]
# each item in this list contains the information of one format of aligning the old and new lines.
# a: index of old lines(blank lines excluded & begin from 0).
# b: index of new lines(blank lines excluded & begin from 0).
# c: index of old lines(blank lines included & begin from 1). (PRINTPATH enabled)
# d: index of new lines(blank lines included & begin from 1). (PRINTPATH enabled)
# e: minimum different lines when the c line and the d line are aligned.
# f: index of previous aligned lines. (PRINTPATH enabled)
 
    oldLineNum = 0
    for eachLine in oldFile:
        oldLineNum += 1
        if not eachLine.isspace():
            oldLines += 1
            oldContents.append([oldLineNum, string.strip(eachLine)])
 
    newLineNum = 0
    for eachLine in newFile:
        newLineNum += 1
        if not eachLine.isspace():
            newLines += 1
            newContents.append([newLineNum, string.strip(eachLine)])    
 
    for i in range(oldLines):       
        for j in range(newLines):
            value = 0
            equal = (oldContents[i][1] == newContents[j][1])
            if j == 0:
                if equal:
                    value = 1
                    commLen.append([1])
                else:
                    commLen.append([0])
            elif i == 0:
                if equal:
                    value = 1
                    commLen[0].append(1)
                else:
                    commLen[0].append(0)
            else:
                if equal:
                    value = commLen[i-1][j-1] + 1
                else:
                    value = max(commLen[i-1][j], commLen[i][j-1])
                commLen[i].append(value)
            if equal and value > 0:
                if PRINTPATH:
                    if len(minDiffs) < value:
                        minDiffs.append([[i,j,oldContents[i][0],newContents[j][0]]])
                    else:
                        minDiffs[value-1].append([i,j,oldContents[i][0],newContents[j][0]])
                else:
                    if len(minDiffs) < value:
                        minDiffs.append([[i,j]])
                    else:
                        minDiffs[value-1].append([i,j])
 
    del commLen
    del oldContents
    del newContents
 
    if PRINTPATH:
        minDiffs.append([[oldLines,newLines,oldLineNum,newLineNum]])
    else:
        minDiffs.append([[oldLines,newLines]])
 
    for i in range(len(minDiffs[0])):
        minValue = max(minDiffs[0][i][0], minDiffs[0][i][1])
        minDiffs[0][i].append(minValue) 
        if PRINTPATH:
            minDiffs[0][i].append(0)
 
    minDiffsNum = len(minDiffs)
    for i in range(1, minDiffsNum):
        curMinDiffNum = len(minDiffs[i])
        prevMinDiffNum = len(minDiffs[i-1])
        for j in range(curMinDiffNum):
            minValue = oldLines + newLines
            final = 0
            for k in range(prevMinDiffNum):
                if minDiffs[i][j][0] > minDiffs[i-1][k][0] and minDiffs[i][j][1] > minDiffs[i-1][k][1]:
                    temp = max(minDiffs[i][j][0]-minDiffs[i-1][k][0]-1, minDiffs[i][j][1]-minDiffs[i-1][k][1]-1)
                    if PRINTPATH:
                        temp += minDiffs[i-1][k][4]
                    else:
                        temp += minDiffs[i-1][k][2]
                    if temp < minValue:
                        minValue = temp
                        final = k         
            minDiffs[i][j].append(minValue)
            if PRINTPATH:
                minDiffs[i][j].append(final)
 
    if PRINTPATH:
        row = len(minDiffs) - 1
        column = 0
        print "/*begin path*/"
        while row >= 0:
            print minDiffs[row][column][2], ' ',
            print minDiffs[row][column][3]
            column = minDiffs[row][column][5]
            row -= 1
        print "/*end path*/"
    
    if PRINTPATH:
        print fileName, " min diff lines ", minDiffs[len(minDiffs)-1][0][4]
    else:
        print  fileName, " min diff lines ", minDiffs[len(minDiffs)-1][0][2]
    del minDiffs
    
def totalLines(filePath):
    try:
        f = open(filePath, 'r')
    except IOError, e:
        print
        print e
        return None
 
    lines = 0
    for eachLine in f:
        if not eachLine.isspace():
            lines += 1
    f.close()
    return lines
 
def main():
    oldRoot = "old"
    newRoot = "new"
    oldFiles = []
    newFiles = []
    for root, dirs, files in os.walk(oldRoot):
        for i in range(len(files)):
            oldFiles.append(join(root[4:], files[i]))
    
    for root, dirs, files in os.walk(newRoot):
        for i in range(len(files)):
            newFiles.append(join(root[4:], files[i]))
 
    oldFile = ""
    newFile = ""
 
    for file in oldFiles:
        if file in newFiles:
            newFiles.remove(file) 
            try:
                oldFile = open(join(oldRoot, file), 'r')
                newFile = open(join(newRoot, file), 'r')
            except IOError, e:
                if not oldFile.close:
                    oldFile.close()
                print e
                raw_input('Press ENTER key to exit')
                return None
            calDiff(oldFile, newFile, file)
            oldFile.close()
            newFile.close()
        else:
            result = totalLines(join(oldRoot, file))
            if result is not None:
                print file, " is deleted. Total lines : ", result
 
    for file in newFiles:
        result = totalLines(join(newRoot, file))
        if result is not None:
            print file, " is added. Total lines : ", result
            
    raw_input('Press ENTER key to exit')
 
 
if __name__ == '__main__':
    main()