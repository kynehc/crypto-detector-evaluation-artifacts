import sys
import re
import pathlib
import os
import pickle
from collections import defaultdict

rulemap={
    '1':'Found broken crypto schemes',
    '2':'Found broken hash functions',
    '3':'Used constant keys in code',
    '4':'Uses untrusted TrustManager',
    '5':'Used export grade public Key',
    '6':'Used untrusted HostNameVerifier',
    '7':'Used HTTP Protocol',
    '8':'Used < 1000 iteration for PBE',
    '9':'Found constant salts in code',
    '10':'Found constant IV in code',
    '11':'Found predictable seeds in code',
    '12':'Should check HostnameVerification manually',
    '13':'Used untrusted PRNG',
    '14':'Used Predictable KeyStore Password'
}

rule_num_map = {}

def sanitizer(item):
    raw = item.split(" in ");

    errorStat = raw[0][3:]
    tmp = raw[1].split("::")
    clazzmethod = tmp[0].split(":")
    className = clazzmethod[0].replace("<", '')
    methodName = clazzmethod[1].split(')')[0]+')'

    return className, methodName, errorStat

def addLogDict(logDict, ruleName, apkName, className, methodName, errorName):
    if ruleName not in rule_num_map:
        rule_num_map[ruleName] = 1
    else:
        rule_num_map[ruleName] += 1

    if ruleName not in logDict:
        logDict[ruleName] = {className: {methodName: {apkName: [errorName]}}}
    elif className not in logDict[ruleName]:
        logDict[ruleName][className] = {methodName: {apkName: [errorName]}}
    elif methodName not in logDict[ruleName][className]:
        logDict[ruleName][className][methodName] = {apkName: [errorName]}
    elif apkName not in logDict[ruleName][className][methodName]:
        logDict[ruleName][className][methodName][apkName] = [errorName]
    else:
        logDict[ruleName][className][methodName][apkName].append(errorName)

def logParse(logDirName, logName, logDict):
    #parse one apk file
    with open(os.path.join(logDirName, logName)) as f:
        content = f.read()

    apkName = logName.split('.txt')[0]

    errors = re.split('=*\n', content)
    for i in range(len(errors)):
        line = errors[i]
        if re.match("\*\*\*Violated Rule [0-9]{1,2}:", line):
            errorName = ""
            methodName = ""
            className = ""
            ruleName = re.findall(r"\d{1,2}", line)[0]

            # for rule 1|2|3|5|7|8|9|10|11|14
            if re.match("\*\*\*Violated Rule (1|2|3|5|7|8|9|10|11|14):", line):
                nextline = errors[i+1]

                className, methodName, errorStat = sanitizer(nextline)
                errorName = errorStat
                addLogDict(logDict, ruleName, apkName, className, methodName, errorName)
                continue
            
            # for rule 4
            elif re.match("\*\*\*Violated Rule 4:", line):
                nextline = errors[i+1]
                errorName = nextline[3:]
                if "java.security.cert.CertificateException" in nextline:
                    className = nextline.split(" method of ")[1].split("::")[0]
                    methodName = "check(Client|Server)Trusted"
                else:
                    methodName, className = nextline.split("Other Sources in ")[1].split(" method of ")
                    className = className.split(" in ")[0].split("::")[0]
            
            # for rule 6
            elif re.match("\*\*\*Violated Rule 6:", line):
                nextline = errors[i+1]
                errorName = nextline[3:]
                methodName = "verify"
                className = nextline.split(" in ")[1].split("::")[0]
            
            # for rule 12, 13
            elif re.match("\*\*\*Violated Rule (12|13):", line):
                nextline = errors[i+1]
                errorName = nextline[3:]
                
                clazzmethod = nextline.split(' in <')[1].split('::')[0].split(':')
                className = clazzmethod[0]
                methodName = clazzmethod[1].split(')')[0]+')'
            
            addLogDict(logDict, ruleName, apkName, className, methodName, errorName)

def saveLogDict(logDict, outDirName):
    for className in logDict:
        with open("{}/{}".format(outDirName, className.split('\n')[0]), "w") as errFile:
            for methodName in logDict[className]:
                errFile.write("----------------------------------------------------------------------\n")
                errFile.write("Method: {}\n".format(methodName))
                errFile.write("Apk Num: {}".format(len(logDict[className][methodName])))
                for apkName in logDict[className][methodName]:
                    errFile.write("\nApk: {}\n".format(apkName))
                    for errorName in logDict[className][methodName][apkName]:
                        errFile.write("Error: {}\n".format(errorName))

def saveStats(logDict):
    with open('Statistic', "w") as statFile:
        statFile.write("Total Class Num: {}\n\n".format(len(logDict)))
        # sort by Apk numbers for each class-method
        for l,c,m in sorted([(len(logDict[c][m]),c,m) for c in logDict for m in logDict[c]] , reverse=True):
            statFile.write("Apk Num:{}\n".format(l))
            statFile.write("Class: {}\n".format(c))
            statFile.write("Method: {}\n\n".format(m))
        print("save Stats.")

def saveRuleStats(logDict, dirName):
    pathlib.Path(dirName).mkdir(parents=True, exist_ok=True)
    totalCount = 0
    for ruleName in logDict:
        with open("{}/rule{}".format(dirName, ruleName), "w") as statFile:
            statFile.write("Rule: {} {}\n".format(ruleName, rulemap.get(ruleName)))
            statFile.write("\n")
            ruleCount = 0
            methCount = 0
            for l,c,m in sorted([(len(logDict[ruleName][c][m]),c,m) for c in logDict[ruleName] for m in logDict[ruleName][c]] , reverse=True):
                cmCount = 0
                methCount += 1
                
                statFile.write("------------------------------------------------\n")
                statFile.write("#{}\n".format(methCount))
                statFile.write("Class: {}\n".format(c))
                statFile.write("Method:{}\n".format(m))
                statFile.write("Apk Num:{}\n".format(l))
                
                for apk in logDict[ruleName][c][m]:
                    statFile.write("\nApk:{}\n".format(apk))

                    for err in logDict[ruleName][c][m][apk]:
                        statFile.write("Err: {}\n".format(err))
                        cmCount += 1
                        ruleCount += 1
                        totalCount += 1
                statFile.write("\nMisuse Num:{}\n".format(cmCount))
            statFile.write("------------------------------------------------\n")
            statFile.write("\nrule {} count overall {} misuses".format(ruleName, rule_num_map[ruleName]))
            statFile.write("\nrule {} count unique {} misuses".format(ruleName, ruleCount))
            statFile.write("\nunique methods {}".format(methCount))
            statFile.write("\nunique apks {}".format(len(logDict[ruleName])))

            print("save rule {} Stats".format(ruleName))
    print("Total misuse number: {}".format(sum(rule_num_map.values())))


def savePickle(logDict):
    with open('LogDict.pkl', 'wb') as pklFile:
        pickle.dump(logDict, pklFile)
        print("save Pickle.")


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: logParser.py <input-log-dir> <output-dir>")
        exit(-1)
    
    # prepare output directory
    outDirName = sys.argv[2]
    # pathlib.Path(outDirName).mkdir(parents=True, exist_ok=True)

    # parse log directory
    logDirName = sys.argv[1]
    logFiles = os.listdir(logDirName)
    
    # nested_dict = lambda: defaultdict(nested_dict)
    # # nested structure: logDict[ruleName][className][methodName][apkName] = errorName
    # logDict = nested_dict()
    logDict = {}
    
    for logFile in logFiles:
        logParse(logDirName, logFile, logDict)
    
    # saveStats(logDict)
    # savePickle(logDict)
    # saveLogDict(logDict, outDirName)
    saveRuleStats(logDict, outDirName)



