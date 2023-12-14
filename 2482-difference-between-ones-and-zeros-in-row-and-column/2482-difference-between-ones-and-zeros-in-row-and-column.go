func onesMinusZeros(grid [][]int) [][]int {
    rowCount := make([]int, len(grid))
    colCount := make([]int, len(grid[0]))
    
    for i, row := range grid  {
        for j, num := range row {
            toAdd := num
            if toAdd == 0 {
                toAdd = -1
            }
            
            rowCount[i] += toAdd
            colCount[j] += toAdd
        }
    }
    
    result := make([][]int, len(grid))
    for i, row := range grid {
        result[i] = make([]int, len(row))
        for j := range row {
            result[i][j] = rowCount[i] + colCount[j]
        }
    }
    
    return result
}