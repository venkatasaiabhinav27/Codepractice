/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL)
            return false;
        unordered_set<ListNode*> address;
        address.insert(head);
        while (head->next != NULL) {
            if (address.find(head->next) == address.end()) {
                address.insert(head->next);
            } else {
                return true;
            }
            head = head->next;
        }
        return false;
    }
};