#!/usr/bin/python3
import sys
import re
import pathlib
import os
import pickle
from collections import defaultdict

def emptyNewLine(line):
    # check if line is empty with only new line char
    if len(line) == 1 and line[0] == "\n":
        return True
    return False

def logParse(logDirName, logName, logDict, ruleDict):
    #parse one apk file
    inFindings = False
    inMethod = False
    inError = False

    apkName = logName.split('.log')[0]
    className = ""
    methodName = ""

    errorType = ""
    errorRule = ""
    errorReason = ""
    errorStmt = ""
    

    inline = ""
    prevLine = ""

    lineNum = 0
    errNum = 0
    errFile = ""

    with open(os.path.join(logDirName, logName)) as infile:
        while True:
            prevLine = inline
            inline = infile.readline()

            if not inline:
                break

            lineNum += 1

            if inline.startswith("Findings in Java Class:"):
                inFindings = True
                className = inline.replace("Findings in Java Class: ", "")
                # print("inFindings @ line", lineNum)

            if inMethod:
                
                if inError:
                    if emptyNewLine(inline):
                        inError = False
                        
                        logDict[apkName][className][methodName][errorType][errorRule][errorReason]=errorStmt
                        ruleDict[errorRule][className][methodName][errorType][errorReason][apkName]=errorStmt
                        # print("errorRule {}".format(errorRule))
                        # print("errorType {}".format(errorType))
                        # print("className {}".format(className.strip()))
                        # print("methodName {}".format(methodName.strip()))
                        # print("apkName {}".format(apkName))
                        # print("errorReason {}".format(errorReason.strip()))
                        # print("errorStmt {}".format(errorStmt))

                    else:
                        # might want to normalize the "Object #[a-f0-9]{64}" and "varReplacer[0-9]{5}" here
                        # errFile.write(re.sub("^[\t]+", "", inline))
                        if 'at statement:' in inline:
                            errorStmt = re.sub("^[\t]+", "", inline).strip()
                        else:
                            errorReason = re.sub("^[\t]+", "", inline).strip()
                        # errorName += re.sub("^[\t]+", "", inline)

                else: # not inError
                    if re.match("^\t\t[a-zA-Z]+Error", inline):
                        inError = True
                        errNum += 1
                        errorName = re.sub("^\t\t", "", inline)
                        errorType = errorName.split(' ')[0]
                        errorRule = errorName.split('for',1)[1].split(' ')[1].strip()
                        # print("errorRule {}".format(errorRule))
                        # print("errorType {}".format(errorType))
                        # print("inError @ line", lineNum)

                if emptyNewLine(inline): 
                    if emptyNewLine(prevLine):
                        inMethod = False
                        # print("out of inMethod @ line", lineNum)

            else: # not inMethod
                if inline.startswith("\t in Method:"):
                    inMethod = True
                    methodName = inline.replace("\t in Method: ", "")
                    # print("inMethod @ line", lineNum)

def saveLogDict(logDict, outDirName):
    for className in logDict:
        with open("{}/{}".format(outDirName, className.split('\n')[0]), "w") as errFile:
            for methodName in logDict[className]:
                errFile.write("----------------------------------------------------------------------\n")
                errFile.write("Method: " + methodName)
                errFile.write("Apk Num: {}".format(len(logDict[className][methodName])))
                for apkName in logDict[className][methodName]:
                    errFile.write("\nApk: " + apkName + '\n')
                    for errorName in logDict[className][methodName][apkName]:
                        errFile.write("Error: " + errorName)

def saveStats(logDict):
    with open('Statistic', "w") as statFile:
        statFile.write("Total Class Num: {}\n\n".format(len(logDict)))
        # sort by Apk numbers for each class-method
        for l,c,m in sorted( [ (len(logDict[c][m]),c,m) for c in logDict for m in logDict[c] ] , reverse=True):
            statFile.write("Apk Num:{}\n".format(l))
            statFile.write("Class: " + c)
            statFile.write("Method: " + m + '\n')
        print("save Stats.")

def saveRuleStats(ruleDict, numDict, outDirName):
    # go through once to get the error with max number of apks in a rule-class-method 
    for errorRule in ruleDict:
        for className in ruleDict[errorRule]:
            for methodName in ruleDict[errorRule][className]:
                maxnum = 0
                for errorType in ruleDict[errorRule][className][methodName]:
                    for errorReason in ruleDict[errorRule][className][methodName][errorType]:
                        apknum = len(ruleDict[errorRule][className][methodName][errorType][errorReason])
                        maxnum = apknum if apknum > maxnum else maxnum
                numDict[errorRule][className][methodName] = maxnum
    
    for errorRule in ruleDict:
        with open("{}/{}".format(outDirName, errorRule.strip()), "w") as errFile:
            count = 0
            # numDict store the max number for each class-method in a rule, we write class-method with bigger number first
            for num, className, methodName in sorted( [(numDict[errorRule][className][methodName], className, methodName) for className in numDict[errorRule] for methodName in numDict[errorRule][className] ], reverse=True):
                errFile.write("----------------------------------------------------------------------\n")
                count += 1
                errFile.write("#{}\n".format(count))
                errFile.write("Class: " + className)
                errFile.write("Method: " + methodName)
                errFile.write("\n")
                tmp = ruleDict[errorRule][className][methodName]
                # sort by apk numbers for all errors in a class-method:
                # under specific rule-class-method dictionary: tmp = ruleDict[errorRule][className][methodName]
                # for-loop each errorReason in each errorType, take (number of apks, errorType, errorReason) as tuple in a list then sort this list in descending order
                for num, etype, ereason in sorted( [ (len(tmp[etype][ereason]), etype, ereason) for etype in tmp for ereason in tmp[etype] ] , reverse=True):
                    errFile.write("Error Type: {}\n".format(etype))
                    errFile.write("Error Reason: {}\n".format(ereason))
                    errFile.write("Apk Num: {}\n".format(num))
                    for apkName in tmp[etype][ereason]:
                        errFile.write("{:<59} => {}\n".format(apkName, tmp[etype][ereason][apkName]))
                    errFile.write("\n")

def savePickle(logDict):
    with open('LogDict.pkl', 'wb') as pklFile:
        pickle.dump(logDict, pklFile)
        print("save Pickle.")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: logParser.py <input-log-dir> <output-dir>")
        exit(-1)
    
    # prepare output directory
    outDirName = sys.argv[2]
    pathlib.Path(outDirName).mkdir(parents=True, exist_ok=True)
    
    # parse log directory
    logDirName = sys.argv[1]
    logFiles = os.listdir(logDirName)

    #define nested_dict
    nested_dict = lambda: defaultdict(nested_dict)
    
    #nested structure: logDict[apkName][className][methodName][errorType][errorRule][errorReason]=errorStmt
    logDict = nested_dict()
    #nested structure: ruleDict[errorRule][className][methodName][errorType][errorReason][apkName]=errorStmt
    ruleDict = nested_dict()
    #nested structure: numDict[errorRule][className][methodName] = maxnum
    numDict = nested_dict()

    for logFile in logFiles:
        logParse(logDirName, logFile, logDict, ruleDict)
    
    # saveStats(logDict)
    # savePickle(logDict)
    # saveLogDict(logDict, outDirName)
    saveRuleStats(ruleDict, numDict, outDirName)
