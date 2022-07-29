# Recursively ---------------------------------------------------------
# Average: Time: O(log(n)) | Space: O(log(n)) 
# Worst: Time: O(n) | Space: O(n)
# ---------------------------------------------------------------------
def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))

def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    else:
        return closest


# Iteratively ----------------------------------------------------------
# Average: Time: O(log(n)) | Space: O(1) 
# Worst: Time: O(n) | Space: O(1)
# ----------------------------------------------------------------------

def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))

def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest