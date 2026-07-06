/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include<stdlib.h>
int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int*result=malloc(nums1Size*sizeof(int));
    int*stack=malloc(nums2Size*sizeof(int));
    int top=-1;
    int map[10001];
    for(int i=0;i< nums2Size;i++)
    {
        int curr=nums2[i];
        
        while(top!=-1 && curr>stack[top]){
            int x=stack[top--];
            map[x]=curr;

        }
        stack[++top]=curr;

    }
    while(top!=-1){
        map[stack[top--]]=-1;
    }
    for(int i=0;i<nums1Size;i++){
        result[i]=map[nums1[i]];
    }
    *returnSize=nums1Size;
    free(stack);
    return result;



}