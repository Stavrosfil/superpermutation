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

def calc(l = []):
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

# def createIterativeTree(root, level):
#     tmp = root
#     createTree(root, level)
#     while level < N:
#         for i in range(len(tmp.children)):
#             createTree(tmp.children[i], level + 1)

def createTree(root, level):
    if level < N:
        nums = removeList(range(N), root.usedNums)
        # print(nums)
        while len(nums) > 0:
            for i in sorted(nums):
                tmp = node()
                tmp.value = i + 0
                tmp.parent = root
                tmp.usedNums = root.usedNums + []
                tmp.usedNums.append(i)
                tmp.level = level
                nums.remove(i)
                root.children.append(tmp)
            for i in range(len(root.children)):
                createTree(root.children[i], level + 1)
            
            
def calculate(root):
    answer = ''
    tmp = root
    while tmp.level < N - 1:
        answer += str(tmp.children[0].value)
        tmp = tmp.children[0]
    print(answer)


def main():
    root1 = node()
    permutationList = createPermutations(N)
    calc(permutationList)
    # createTree(root1, 0)
    # print(len(root1.children))
    # for i in range(len(root1.children)):
    #     tempNode = root1.children[i]
    #     for j in range(len(tempNode.children)):
    #         for k in range(len(tempNode.children[j].children)):
    #             tempNode2 = tempNode.children[j].children[k]
    #             print(tempNode2.value)
    # calculate(root1)


if __name__ == "__main__":
    main()

# createPermutations(4)
