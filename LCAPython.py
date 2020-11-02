class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

path1 = []
path2 = []
root = Node

def LCA(node1, node2):
    global path1
    global path2
    path1 = []
    path2 = []
    return getLCA(root, node1, node2)

def getLCA(root, node1, node2):
    if(getPath(root, node1, path1) and getPath(root, node2, path2)):
        if (len(path1) > len(path2)): iMax = len(path2)
        else: iMax = len(path1)
        for i in range(iMax):
            index1 = path1[i]
            index2 = path2[i]
            if(index1 != index2):
                break
            if(i == iMax - 1):
                if(i == iMax - 1):
                    lca = index1
                    return lca
        lca = path1[i-1]
        return lca
    else:
        print ("Nodes are not present in the tree")
        return -1

def getPath(root, endNode, path):
    if(root == None):
        return False
    path.append(root.value)

    if(root.value == endNode):
        return True

    if(root.left != None and getPath(root.left, endNode, path)):
        return True

    if(root.right != None and getPath(root.right, endNode, path)):
        return True

    path.pop()
    return False


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
#root.left.right.left = Node(8)
#root.left.right.right = Node(9)
#root.right.right.left = Node(10)
#root.right.right.right = Node(11)
#root.left.right.right.left = Node(12)
#root.left.right.right.right = Node(13)

#print ("LCA of nodes with values 6 and 10 is " + str(LCA(6, 10))) #should be 3
#print ("LCA of nodes with values 8 and 9 is " + str(LCA(8, 9))) #should be 5
#print ("LCA of nodes with values 7 and 11 is " + str(LCA(7, 11))) #should be 7
#print ("LCA of nodes with values 12 and 3 is " + str(LCA(12, 3))) #should be 1