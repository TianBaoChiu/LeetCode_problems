class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 建立各個節點
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# 將結點指向下一個節位置
node1.next = node2
node2.next = node3
node3.next = node4

# 建立head節點
head = node1

# 建立current node
current_node = head

# 當前current_node = node1


# 歷遍整個串列，透過移動current node
while current_node:
    print(current_node.val)
    current_node = current_node.next
