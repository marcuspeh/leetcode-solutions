func transpose(matrix [][]int) [][]int {
    result := make([][]int, len(matrix[0]))
    for i := range matrix[0] {
        result[i] = make([]int, len(matrix))
    }

    for i, row := range matrix {
        for j, item := range row {
            result[j][i] = item
        }
    }

    return result
}
