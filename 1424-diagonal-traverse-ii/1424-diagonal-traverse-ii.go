func findDiagonalOrder(nums [][]int) []int {
    maxRow := 0
    for _, row := range nums {
        maxRow = max(maxRow, len(row))
    }
    
    diagonals := make([][]int, len(nums) + maxRow)
    count := 0
    for i, row := range nums {
        for j, num := range row {
            diagonals[i + j] = append(diagonals[i + j], num)
            count++
        }
    }
    
    result := make([]int, count)
    curr := 0
    for _, diagonal := range diagonals {
        for i := len(diagonal) - 1; i >= 0; i-- {
            result[curr] = diagonal[i]
            curr++
        }
    }
    
    return result
}