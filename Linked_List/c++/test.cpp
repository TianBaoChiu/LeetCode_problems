#include <iostream>

// 定義鏈表節點結構體
struct ListNode
{
    int val;
    ListNode *next;

    // 構造函數
    ListNode(int x) : val(x), next(nullptr) {}
};

int main()
{
    // 建立各個節點
    ListNode *node1 = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    ListNode *node3 = new ListNode(3);
    ListNode *node4 = new ListNode(4);

    // 將節點指向下一個節點
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;

    // 建立頭節點
    ListNode *head = node1;

    // 建立當前節點
    ListNode *current_node = head;

    // 歷遍整個鏈表，透過移動current_node
    while (current_node != nullptr)
    {
        std::cout << current_node->val << " ";
        current_node = current_node->next;
    }
    std::cout << std::endl;

    // 釋放動態分配的節點內存
    delete node4;
    delete node3;
    delete node2;
    delete node1;

    return 0;
}