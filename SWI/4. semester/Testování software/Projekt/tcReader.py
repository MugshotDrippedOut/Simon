# look into every file in every directory of the given path and give back number of times the word "TC" is found in the robot file

import os

def printRobotFiles(path, exceptionDir = "Resources", fileEnd = ".robot", lineStart = "TC"):
    if os.path.exists(path) == False:
        print("Path does not exist")
        return
    if fileEnd == ".robot":
        print("Looking for robot files in " + path)
    elif fileEnd == ".md":
        print("Looking for markdown files in " + path)
    else:
        print("Looking for files with ending " + fileEnd + " in " + path)
    count = 0
    for root, dirs, files in os.walk(path):
        if exceptionDir in root:
            continue
        for file in files:
            if file.endswith(fileEnd):
                print(os.path.join("    " + file))
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    try:
                        for line in f:
                            if "TC" in line and line.startswith(lineStart):
                                count += line.count("TC")
                                print(os.path.join("        " + line)[:-1])
                    except Exception as e:
                        print("Error reading file"+ str(e))
    print("\nNumber of TCs found: " + str(count))


exceptionDir = "Resources"

path = input("Enter the path (default _projekt): ")
if path == "":
    path = "_projekt"
elif path == "q":
    exit()

fileEnd = input("m - .md files ,\nr - .robot files (default),\nq - quit\n")
if fileEnd == "m":
    fileEnd = ".md"
elif fileEnd == "r":
    fileEnd = ".robot"
elif fileEnd == "q":
    exit()
else:
    fileEnd = ".robot"
if fileEnd == ".robot":
    lineStart = input("1 - TC (default),\n2 - ## TC,\n3 - custom\nq - quit\n")
    if lineStart == "1" or lineStart == "":
        lineStart = "TC"
    elif lineStart == "2":
        lineStart = "## TC"
    elif lineStart == "q":
        exit()
    elif lineStart == "c":
        lineStart = input("Enter the custom line start: ")
        if lineStart == "q":
            exit()
if fileEnd == ".md":
    lineStart = input("1 - TC,\n2 - ## TC(default),\n3 - custom\nq - quit\n")
    if lineStart == "1":
        lineStart = "TC"
    elif lineStart == "2" or lineStart == "":
        lineStart = "## TC"
    elif lineStart == "q":
        exit()
    elif lineStart == "c":
        lineStart = input("Enter the custom line start: ")
        if lineStart == "q":
            exit()


printRobotFiles(path, exceptionDir, fileEnd, lineStart)