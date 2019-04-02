bool checkPossibility(int* nums, int numsSize) {
    int index = -1;
    for (int i = 0; i < numsSize - 1; i++ ){
        if (nums[i] > nums[i+1]) {
            if (-1 != index) {
                return false;
            }
            index = i;
        }
    }
    
    return -1 == index || 0 == index || numsSize - 2 == index || nums[index-1] <= nums[index+1] || nums[index] <= nums[index+2];
}