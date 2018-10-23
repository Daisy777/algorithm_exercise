import java.util.HashMap;

class Solution {
    public int arrayNesting(int[] nums) {
        boolean[] visited = new boolean[nums.length];
        for (int i=0; i<nums.length; i++) {
            visited[i] = false;      
        }

        int longest = 0;
        for (int i=0; i<nums.length; i++) {
            int length = 0;
            int index = i;
            while(!visited[index]) {
                visited[index] = true;
                index = nums[index];
                length ++;
            }

            if (length > longest) {
                longest = length;
            }
        }

        return longest;
    }
}