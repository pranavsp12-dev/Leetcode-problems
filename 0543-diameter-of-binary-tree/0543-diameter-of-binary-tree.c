/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int d=0;
 int max(int l, int r)
 {
    if(l>r){
        return l;
    }
    else{
        return r;
    }
 }
 int height(struct TreeNode* root){
    if(root==NULL){
        return 0;
    }
    int left=height(root->left);
    int right=height(root->right);
    d=max(d,left+right);
    return 1+max(left,right);
 }
int diameterOfBinaryTree(struct TreeNode* root) {
 d=0;
height(root);
return d;
    
}