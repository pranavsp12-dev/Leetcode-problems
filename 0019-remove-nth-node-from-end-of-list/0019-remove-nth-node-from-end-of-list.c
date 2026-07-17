/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if(head==NULL || head->next==NULL){
        return NULL;
    }
    struct ListNode temp;
     temp.next=head;
    struct ListNode* s=&temp;
    struct ListNode* f=&temp;
    for(int i=0;i<n+1;i++){
        f=f->next;
    }
    while(f!=NULL){
        s=s->next;
        f=f->next;
    }
    s->next=s->next->next;
    return temp.next;
   
    

    
}