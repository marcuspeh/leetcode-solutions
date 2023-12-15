func largestSubmatrix(matrix [][]int) int {
    prev := []int{}
    curr := make([]int, len(matrix[0]))
    result := 0
    
    for _, row := range matrix {
        prev = curr
        curr = make([]int, len(matrix[0]))
        
        for j, element := range row {
            if element == 0 {
                continue
            }
            
            curr[j] = prev[j] + 1
        }
        
        currCopy := make([]int, len(matrix[0]))
        copy(currCopy, curr)
        sort.Slice(currCopy, func(i, j int) bool {
            return currCopy[i] > currCopy[j]
        })
        
        for k, count := range currCopy {
            result = max(result, (k + 1) * count)            
        }
    }
    
    return result
}