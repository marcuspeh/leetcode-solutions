func destCity(paths [][]string) string {
    cache := map[string]int{}
    
    for _, path := range paths {
        cityA := path[0]
        cityB := path[1]
                      
        cache[cityA] += 1        
        
        _, hasB := cache[cityB]
        if !hasB {
            cache[cityB] = 0
        }
    }
    
    for city, count := range cache {
        if count == 0 {
            return city
        }
    }
    
    return ""
}