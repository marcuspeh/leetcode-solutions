class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> lst = new ArrayList<>();
        for (int[] var: intervals) {
            lst.add(var);
        }
        
        // Find index to insert
        int start = 0;
        int end = lst.size();
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            
            if (lst.get(mid)[0] < newInterval[0]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        lst.add(start, newInterval);
        
        // Combine result
        List<int[]> result = new ArrayList<>();
        result.add(lst.get(0));
        for (int i = 1; i < lst.size(); i++) {        
            int lastIndex = result.size() - 1;
            if (result.get(lastIndex)[1] < lst.get(i)[0]) {
                result.add(lst.get(i));
            } else {
                result.get(lastIndex)[1] = Math.max(result.get(lastIndex)[1], lst.get(i)[1]);
            }
        }
        
        return result.toArray(new int[result.size()][2]);
    }
}