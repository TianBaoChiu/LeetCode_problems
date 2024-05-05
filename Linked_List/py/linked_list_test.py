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


# ---歷遍整個串列，透過移動current node
print("歷遍節點")
while current_node:
    print(current_node.val)
    current_node = current_node.next


# ---查找節點

# 先將current node回到head
current_node = head
# 建立目標
target_val = 3
print("查找節點")
while current_node:
    if current_node.val == target_val:
        print("Find the target value")
        break
    current_node = current_node.next

# ---插入節點
# 先將current node回到head
current_node = head
print("插入節點")
while current_node:
    if current_node.val == 2:
        new_node = ListNode(5)
        # 將新插入的節點下一個位置指向原本的下一個節點位置
        new_node.next = current_node.next
        # 將當前節點的下一個位置指向新插入節點的位置
        current_node.next = new_node
    current_node = current_node.next

current_node = head
while current_node:
    print(current_node.val)
    current_node = current_node.next

# ---刪除節點
# 先將current node回到head
current_node = head
pre_node = None
del_val = 3
print("刪除節點")
while current_node:
    if current_node.val == del_val:
        # 判斷是不是對於頭節點作刪除，如果pre_node有值，那代表不是對頭節點刪除
        # 這邊由於pre_node會和當前節點的前一個節點共用記憶體位置，所以對pre_node作變更，會等於對當前節點的前一個節點作變更
        if pre_node:
            pre_node.next = current_node.next
        else:
            head = current_node.next
    pre_node = current_node
    current_node = current_node.next
current_node = head
while current_node:
    print(current_node.val)
    current_node = current_node.next
