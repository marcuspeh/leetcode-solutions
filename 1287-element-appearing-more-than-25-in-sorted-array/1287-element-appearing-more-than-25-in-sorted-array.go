func findSpecialInteger(arr []int) int {
    targetCount := len(arr) / 4
    
    count := 0
    curr := arr[0]
    for _, num := range arr {
        if curr != num {
            curr = num
            count = 1
            continue
        }
        
        count++
        
        if count > targetCount {
            break
        }
    }
    return curr
}
