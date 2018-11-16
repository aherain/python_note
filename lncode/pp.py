# class Test(object):
#     num_of_instance = 0
#     def __init__(self, name):
#         self.name = name
#         Test.num_of_instance += 1
#
#
# if __name__ == '__main__':
#     print(Test.num_of_instance)

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

def lookup(root):
    row = [root]
    while row:
        print(row)
        row = [kid for item in row for kid in (item.left, item.right) if kid]

# def deep(root):
#     if not root:
#         return
#     print(root.data)
#     deep(root.left)
#     deep(root.right)


#求树的最大深度
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right))+1

#判断两个树是否相同
def isSameTree(p, q):
    if p == None and q==None:
        return True
    elif p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

#前序中序求后序
pre = 'GDAFEMHZ'
center = 'ADEFGHMZ'
def rebuild(pre, center):
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1: index+1], center[:index])
    cur.right = rebuild(pre[index+1], center[index+1])
    return cur


def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print(root.data)



if __name__ == "__main__":
    lookup(tree)
    deep(rebuild('GDAFEMHZ', 'ADEFGHMZ'))
    print('树的最大深度', maxDepth(tree))