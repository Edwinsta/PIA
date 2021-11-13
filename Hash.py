import subprocess
import argparse
import os
import pickle
import configparser

info = 'File System Baseline Creator with PowerShell- Version 1.0 December 2018'
config = configparser.ConfigParser()
config.read("config.txt")
baseline = config.get("ARGUMENTS", "baseline")
Path = config.get("ARGUMENTS", "Path")
tmp = config.get("ARGUMENTS" , "tmp")

baselineFile = baseline
targetPath   = Path
tmpFile      = tmp

command ="powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder \""+\
          targetPath + "\" -ResultFile \"" + tmpFile  +"\""
powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
if powerShellResult.stderr == None:
    
    baseDict = {}
    
    with open(tmpFile, 'r') as inFile:
        for eachLine in inFile:
            lineList = eachLine.split()
            if len(lineList) == 2:
                hashValue = lineList[0]
                fileName  = lineList[1]
                baseDict[hashValue] = fileName
            else:
                continue

    with open(baselineFile, 'wb') as outFile:
        pickle.dump(baseDict, outFile)
        print("Baseline: ", baselineFile, " Created with:",
              "{:,}".format(len(baseDict)), "Records")
        print("Script Terminated Successfully")
else:
    print("PowerShell Error:", powerShellResult.stderr)


    
    
    
