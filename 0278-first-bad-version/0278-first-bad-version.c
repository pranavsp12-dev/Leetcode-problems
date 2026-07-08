// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    int l=1;
    int r=n;
    //int mid=(l+r)/2;
    
    while(l<r){
        int mid=l+(r-l)/2;
        if(isBadVersion(mid)){
            r=mid;
        }
        else{
            l=mid+1;
        }
    }
    return l;
    
}