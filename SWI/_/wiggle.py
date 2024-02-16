# increase recursion depth
import sys
sys.setrecursionlimit(10000)

def fun(word, rrange = 20, repeatN = 5, addSpace = False):
    wordAdd = word
    space = ""
    for i in range(repeatN):
        for i in range(rrange):
            print(space + word )
            word += wordAdd
            if addSpace:
                space += " "
        for i in range(rrange):
            word = word[:-1]
            space = space[:-1]
            print(space + word)

        
fun("0o", 5, 8, False)