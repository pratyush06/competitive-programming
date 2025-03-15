from dataclasses import dataclass


class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data=data # root node
        self.left=None
        self.right=None
    
    def getData(self):
        return self.data

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    

#Give an algorithm for finding maximum element in binary tree

maxData=0

def findMaxDataInBT(root):
    if not root:
        return maxData
    if root>maxData:
        maxData=root
    findMaxDataInBT(root.left)
    findMaxDataInBT(root.right)
    return maxData


# find max depth of BTrees

def maxDepth(root):
    if not root:
        return 0
    
    return max(maxDepth(root.left), maxDepth(root.right))+1



