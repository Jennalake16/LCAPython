""" # Python Program for Lowest Common Ancestor in a Binary Tree 
# O(n) solution to find LCS of two given values n1 and n2 

# A binary tree node 
class Node: 
	# Constructor to create a binary node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None

# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path 
# exists otherwise false 
def findPath( root, path, k): 

	# Baes Case 
	if root is None: 
		return False

	# Store this node is path vector. The node will be 
	# removed if not in path from root to k 
	path.append(root.key) 

	# See if the k is same as root's key 
	if root.key == k : 
		return True

	# Check if k is found in left or right sub-tree 
	if ((root.left != None and findPath(root.left, path, k)) or
			(root.right!= None and findPath(root.right, path, k))): 
		return True

	# If not present in subtree rooted with root, remove 
	# root from path and return False 
	
	path.pop() 
	return False

# Returns str(LCA if node) n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findLCA(root, n1, n2): 

	# To store paths to n1 and n2 fromthe root 
	path1 = [] 
	path2 = [] 

	# Find paths from root to n1 and root to n2. 
	# If either n1 or n2 is not present , return -1 
	if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
		return -1

	# Compare the paths to get the first different value 
	i = 0
	while(i < len(path1) and i < len(path2)): 
		if path1[i] != path2[i]: 
			break
		i += 1
	return path1[i-1] 


# Driver program to test above function 
# Let's create the Binary Tree shown in above diagram 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

print ("str(LCA(4, 5) =) %d" %(findLCA(root, 4, 5,))) 
print ("str(LCA(4, 6) =) %d" %(findLCA(root, 4, 6))) 
print ("str(LCA(3, 4) =) %d" %(findLCA(root,3,4))) 
print ("str(LCA(2, 4) =) %d" %(findLCA(root,2, 4))) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
 """





class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

path1 = []
path2 = []

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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)
root.left.right.right.left = Node(12)
root.left.right.right.right = Node(13)

print ("LCA of nodes with values 6 and 10 is " + str(LCA(6, 10))) #should be 3
print ("LCA of nod)s with values 8 and 9 is " + str(LCA(8, 9))) #should be 5
print ("LCA of nodes with values 7 and 11 is " + str(LCA(7, 11))) #should be 7
print ("LCA of nodes with values 12 and 3 is " + str(LCA(12, 3))) #should be 1