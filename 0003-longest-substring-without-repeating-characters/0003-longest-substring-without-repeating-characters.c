int lengthOfLongestSubstring(char* s) {
    int freq[128]={0};
    int right=0;
    int left=0;
    int maxlen=0;
    for(int right=0;s[right]!='\0';right++){
        freq[s[right]]++;
        while(freq[s[right]]>1){
            freq[s[left]]--;
            left++;
        }
        int len=right-left+1;
    if(len>maxlen){
        maxlen=len;
        
            }
    
    }
    return maxlen;
    
}