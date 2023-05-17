/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
private:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* nextCurr = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextCurr;
        }
        return prev;
    }

public:
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        ListNode* secondHalf = slow->next;
        slow->next = nullptr;
        secondHalf = reverse(secondHalf);
        
        int result = INT_MIN;
        while (head != nullptr) {
            result = max(result, head->val + secondHalf->val);
            head = head->next;
            secondHalf = secondHalf->next;
        }
        
        return result;
    }
};