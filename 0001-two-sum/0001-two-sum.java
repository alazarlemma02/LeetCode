class Solution {
    // The following is my solution to this problem.
    public int[] twoSum(int[] nums, int target) {
        int answer[] =new int[2];
        for(int i=0;i<=nums.length-1;i++){
            for(int j=1;j<=nums.length-1;j++){
                if((nums[i]+nums[j]) == target && i!=j){
                    answer[0]=i;
                    answer[1]=j;
                    return answer;
                }
            }
        }
       return answer; 
    }
}