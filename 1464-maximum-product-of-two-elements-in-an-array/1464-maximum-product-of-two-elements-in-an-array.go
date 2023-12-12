func maxProduct(nums []int) int {
    largest := 0
    secondLargest := 0
    
    for _, num := range nums {
        if num > largest {
            secondLargest = largest
            largest = num
        } else if num > secondLargest {
            secondLargest = num
        }
    }
    
    return (largest - 1) * (secondLargest - 1)
}