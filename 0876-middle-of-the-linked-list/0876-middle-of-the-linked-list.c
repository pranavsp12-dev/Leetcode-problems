/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode*s=head;
    struct ListNode*f=head;
    if(head==NULL){
        return NULL;
    }
    while(f!=NULL && f->next!=NULL){
        s=s->next;
        f=f->next->next;
    }
    return s;

    
}