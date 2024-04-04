# look into every file in every directory of the given path and give back number of times the word "TC" is found in the robot file

import os

def printRobotFiles(path, exceptionDir = "Resources", fileStart = "TC"):
    if os.path.exists(path) == False:
        print("Path does not exist")
        return
    print("\nRobot files in the given path:")
    count = 0
    for root, dirs, files in os.walk(path):
        if exceptionDir in root:
            continue
        for file in files:
            if file.endswith(".robot"):
                print(os.path.join("    " + file))
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        if "TC" in line:
                            count += line.count("TC")
                            print(os.path.join("        " + line))
    print("\nNumber of TCs found: " + str(count))


path = "Projekt\_projekt"
exceptionDir = "Resources"
path1 = "../"

#printRobotFiles(path1) # insert your path here
printRobotFiles(path) # insert your path here
