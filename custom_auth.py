import sys
import re

def analyzeInput(filepath):
    lines = []
    file = open(filepath, "r")
    for line in file:
        lines.append(line)
    file.close()
    matchValues = []
    regexValues = [r'The desired string IS present in the file[.]', r'[A-z\s]{26}[:][A-x\s]{9}[0-9]{1,}', r'[0-9]{2}.[0-9]{10}[ ][F]', r'[0-9]{2}[ ][%]', r'[0-9]{2,} days [0-9]{1,} hours [0-9]{1,} minutes', r'[0-9]{2}[.][0-9] F', r'[0-9]{2}[.][0-9] F', r'[0-9]{2}[ ][%]', r'[0-9]{2}[ ][%]']
    idx = 0
    for x in regexValues:
        matchVal = re.match(x, lines[idx])
        matchValues.append(matchVal)
        idx += 1
    return matchValues

def runValidation():
    results = analyzeInput("/Users/chandlerdespirlet/Desktop/CUSTOM_OUT.txt")
    failedValues = []
    idx = 0
    for x in results:
        if (x == False):
            failedValues.append("Failed on Case: " + str(idx + 1))
            idx += 1
    return failedValues

def run():
    results = runValidation()
    outFile = open("/Users/chandlerdespirlet/Desktop/custom_sample_data.txt", "w+")
    outFile.write(results)
    outFile.close()

def main():
    run()

if __name__ == '__main__':
    main()