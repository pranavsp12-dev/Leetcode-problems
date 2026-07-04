int minSubArrayLen(int target, int* nums, int numsSize) {
    int left=0;
    int sum=0;
    int length=numsSize+1;
    for(int right=0;right<numsSize;right++){
        sum+=nums[right];
        while(sum>=target){
            int curlen=right-left+1;
            if(curlen<length){
                length=curlen;
            }
            sum-=nums[left];
            left++;

        }
        
    }
    if(length==numsSize+1){
            return 0;
        }
        return length;
    
}