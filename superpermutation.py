import numpy as np
from itertools import permutations

N = 7


class node():

    def __init__(self, value=-1):
        self.value = value
        self.usedNums = []
        self.children = []
        self.parent = None
        self.value = -2
        self.level = 0


def createPermutations(n):
    l = list(permutations(range(1, n+1)))
    ans = []
    tempSum = ''
    for a in l:
        for i in a:
            tempSum += str(i)
        ans.append(tempSum)
        tempSum = ''
    # print(ans)
    return ans


def searchForNumInIterations(cutNum, l):
    for i in range(len(l)):
        item = l[i]
        if item.startswith(cutNum):
            # del l[i]
            return (item, i)
    return ('-1', '-1')


def calc(l=[]):
    finalString = ''
    lastNum = l[0]
    finalString = lastNum
    del l[0]
    # for i in l:
    while len(l) > 0:
        # Loop for each possible substring of 1234
        for j in range(len(lastNum)):
            # If lastNum is 0123, then the first cut_lastNum is 123
            cut_lastNum = lastNum[j+1:]
            # print('cut number: ' + str(cut_lastNum))
            # We look for a number that starts with 123, 23, 3 etc..
            ans = searchForNumInIterations(cut_lastNum, l)
            # print(ans)
            # If there is a suitable number found, the result is not -1
            if ans[0] != '-1':
                numToAppend = ans[0][len(cut_lastNum):]
                finalString += (numToAppend)
                lastNum = ans[0]
                del l[ans[1]]
                break
    print(finalString)
    print(len(finalString))
    print('leek')


def removeList(a, b):
    return list(set(a)-set(b))


def main():
    root1 = node()
    permutationList = createPermutations(N)
    calc(permutationList)


if __name__ == "__main__":
    main()

# createPermutations(4)
