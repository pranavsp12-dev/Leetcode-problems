/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 #include<stdlib.h>
 int max(int l, int r){
    if(l>r){
        return l;
    }
    return r;
 }
 int height(struct TreeNode* root)
 {
    if(root==NULL){
        return 0;
    }
    int left=height(root->left);
    
    int right=height(root->right);
    if(right==-1){
        return -1;
    }
    else if(left==-1){
        return -1;
    }
    else if(abs(left-right)>1){
        return -1;

    }
    else{
        return 1+max(left,right);
    }


 }
bool isBalanced(struct TreeNode* root) {
    int x=height(root);
    if(x==-1){
        return false;
    }
    else{
        return true;
    }

    
}