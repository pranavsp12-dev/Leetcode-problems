/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int max(int l, int r){
    if(l>r){
        return l;
    }
    else{
        return r;
    }
 }
int maxDepth(struct TreeNode* root) {
    if(root==NULL){
        return 0;
    }
    int height=max(maxDepth(root->left),maxDepth(root->right))+1;
    return height;
    
}