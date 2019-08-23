class ListNode:
    def __init__(self, item):
        self.val = item
        self.next = None


def gensinglelist1(data):
    """
    顺序插入
    :param data:
    :return:
    """
    # 实例化一个节点
    prenode = ListNode(0)
    lastnode = prenode
    for item in data:
        node = ListNode(item)
        # 尾节点指向刚插入的
        lastnode.next = node
        # 始终是最后一个节点，每加一个
        lastnode = lastnode.next
    return prenode.next


def printlist(l):
    cur = l
    while cur:
        print(cur.val)
        cur = cur.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        val = l1.val + l2.val
        ansnode = ListNode(val % 10)
        ansnode.next = self.addTwoNumbers(l1.next, l2.next)

        if val >= 10:
            ansnode.next = self.addTwoNumbers(ListNode(1), ansnode.next)
        return ansnode


l1 = gensinglelist1([2, 8, 9])
l2 = gensinglelist1([3, 8, 7])
s = Solution()
printlist(s.addTwoNumbers(l1, l2))
