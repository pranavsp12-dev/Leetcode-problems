/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include<stdlib.h>

int* nextGreaterElements(int* nums, int numsSize, int* returnSize) {
    int *result=malloc( numsSize*sizeof(int));
    int *stack=malloc( numsSize*sizeof(int));
    int top=-1;
    
    for(int i=0;i<2*numsSize;i++){
        int curr=nums[i%numsSize];
        while(top!=-1 &&curr>nums[stack[top]]){
            int x=stack[top--];
            result[x]=curr;
        }
        if(i<numsSize)
        stack[++top]=i;
    }
    while(top!=-1){
        result[stack[top--]]=-1;
    }
    *returnSize=numsSize;
    free(stack);
    return result; 
}