/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().

 */
 #include<stdlib.h>
 struct Queue{
    struct TreeNode *q[2000];
    int front;
    int rear;

 };
//  struct Queue *queue=malloc(sizeof(struct Queue));
//  front=-1;
//  rear=-1;
 int isEmpty(struct Queue *queue){
    if(queue->front==-1){
        return 1;
    }
    return 0;
 }
 int queuesize(struct Queue *queue){
    if(isEmpty(queue)){
        return 0;
    }
    return queue->rear-queue->front+1;
 }
void enqueue(struct Queue *queue,struct TreeNode* node ){
    if(queue->front==-1){
        queue->front=0;
        queue->rear=0;
    }
    else{
        queue->rear++;
    }
    queue->q[queue->rear]=node;
}
struct TreeNode* dequeue(struct Queue *queue){
    if(queue->front==-1 && queue->rear==-1){
        return NULL;
    }
    struct TreeNode*temp=queue->q[queue->front];
    if(queue->front==queue->rear){
        queue->front=-1;
        queue->rear=-1;
    }
    else{
        queue->front++;
    }
    return temp;
}

int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if(root==NULL){
        * returnSize=0;
        * returnColumnSizes=NULL;
        return NULL;

    }
    struct Queue queue;
    queue.front=-1;
    queue.rear=-1;
    enqueue(&queue,root);
    int **ans = malloc(2000 * sizeof(int *));
*returnColumnSizes = malloc(2000 * sizeof(int));
int rows=0;
while(!isEmpty(&queue)){
    int size=queuesize(&queue);
    int *level=malloc(size*sizeof(int));
    for(int i=0;i<size;i++){
        struct TreeNode* node=dequeue(&queue);
        level[i]=node->val;
        if(node->left!=NULL){
          enqueue(&queue,node->left);
        }
        if(node->right!=NULL){
            enqueue(&queue,node->right);
        }
        


    }
    ans[rows]=level;
        (*returnColumnSizes)[rows]=size;
        rows++;
    
}
*returnSize=rows;
return ans;

    
}