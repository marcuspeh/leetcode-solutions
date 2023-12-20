func buyChoco(prices []int, money int) int {
    smallest := 101
    secondSmallest := 101
    
    for _, price := range prices {
        if price < smallest {
            secondSmallest = smallest
            smallest = price
        } else if price < secondSmallest {
            secondSmallest = price
        }
    }
    
    if smallest + secondSmallest > money {
        return money
    }
    return money - smallest - secondSmallest
}