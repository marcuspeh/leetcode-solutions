func getSumAbsoluteDifferences(nums []int) []int {
    prefix := make([]int, len(nums))
    for i, num := range nums {
        if i == 0 {
            prefix[i] = num
            continue
        }
        prefix[i] = prefix[i - 1] + num
    }
    
    result := make([]int, len(nums))
    for i, num := range nums {
        leftSum := prefix[i]
        rightSum := prefix[len(prefix) - 1] - prefix[i]
        
        leftResult := num * (i + 1) - leftSum
        rightResult := rightSum - num * (len(nums) - i - 1)
        
        result[i] = leftResult + rightResult
    }
    
    return result
}