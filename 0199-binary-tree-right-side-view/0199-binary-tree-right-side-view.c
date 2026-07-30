/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 void dfs(struct TreeNode* root,int depth, int* arr,int* returnSize ){
    if(root==NULL){
        return;
    }

if(depth==*returnSize ){
    arr[* returnSize ]=root->val;
     (*returnSize)++;
}
dfs(root->right,depth+1,arr, returnSize );
dfs(root->left,depth+1,arr, returnSize );

 }
int* rightSideView(struct TreeNode* root, int* returnSize) {
    int *arr=malloc(100*sizeof(int));
    if(root==NULL){
        * returnSize=0;
        return NULL;

    }
    * returnSize=0;
    dfs(root, 0, arr,returnSize);
    return arr;
  

    
}