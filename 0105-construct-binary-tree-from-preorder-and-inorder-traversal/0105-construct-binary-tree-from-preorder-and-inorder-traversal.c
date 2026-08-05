/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    if(preorderSize==0 || inorderSize==0){
        return NULL;

    }
    struct TreeNode*root=malloc(sizeof(struct TreeNode));
    root->val=preorder[0];
    int i=0;
    for(i=0;i<inorderSize;i++){
        if(inorder[i]==root->val){
            break;
        }
         
    
    }
    int leftsize=i;
         int rightsize=inorderSize-leftsize-1;

    root->left=buildTree(preorder+1,leftsize,inorder,leftsize);
    root->right=buildTree(preorder+leftsize+1,rightsize,inorder+leftsize+1,rightsize);
    return root;
   
}