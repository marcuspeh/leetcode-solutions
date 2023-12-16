func isAnagram(s string, t string) bool {
    counter := map[rune]int{}
    
    for _, character := range s {
        counter[character]++
    }
    
    for _, character := range t {
        counter[character]--
        
        if counter[character] < 0 {
            return false
        }
    }
    
    for _, count := range counter {
        if count != 0 {
            return false
        }
    }
    
    return true
}