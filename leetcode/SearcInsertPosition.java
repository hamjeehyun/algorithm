

class SearcInsertPosition {
    static int[] nums = {1,3,5,6};
    static int target = 5;


    static private void solutionIterator() {
        for(int i=0; i<nums.length; i++) {
            if(nums[i] >= target) {
                System.out.println("Iterator >>> " + i);
                return;
            }
        }
        System.out.println("Iterator >>> " + nums.length);
    }

    static private void solutionBinarySearch() {
        int start = 0;
        int end = nums.length-1;


        while (start <= end) {
            int mid = (start + end)/2;
            
            if(nums[mid] == target) {
                System.out.println("Binary Search >>> " + mid);
                return;
            }
            else if(nums[mid] > target)
                end = mid-1;
            else
                start = mid+1;
        }
        System.out.println("Binary Search >>> " + start);
    }


    public static void main(String[] args) {
        solutionIterator();
        solutionBinarySearch();
    }
}

