/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int countnodes(struct TreeNode* root){
    if(root==NULL){
        return 0;
    }
    return 1+ countnodes(root->left)+countnodes(root->right);
 }
 void inorder(struct TreeNode*root,int*arr,int *i){
    
    if(root==NULL){
        return ;
    }
    inorder(root->left,arr,i);
    
    arr[*i]=root->val;
    (*i)++;
    inorder(root->right,arr,i);

    


 }
 
int kthSmallest(struct TreeNode* root, int k) {
    int size=countnodes(root);
    int *arr=malloc(sizeof(int)*size);
    int i=0;
    inorder(root,arr,&i);
    return arr[k-1];
    
}