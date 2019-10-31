import sys
from re import match

def analyzeInput(filepath):
    lines = []
    file = open(filepath, "r")
    for line in file:
        lines.append(line)
    file.close()
    matchValues = []
    regexValues = ['', '', '', '', '', '', '', '', '']
    #line1re = ''
    #line2re = ''
    #line3re = ''
    #line4re = ''
    #line5re = ''
    #line6re = ''
    #line7re = ''
    #line8re = ''
    #line9re = ''
    idx = 0
    for x in regexValues:
        matchValues.append(bool(match(r x, lines[idx])))
        idx += 1
    return matchValues

def runValidation(results):
    failedValues = []
    idx = 0
    for x in results:
        if (x == False):
            failedValues.append("Failed on Case: " + str(idx + 1))
            idx += 1
    return failedValues
    
def run(values):
    