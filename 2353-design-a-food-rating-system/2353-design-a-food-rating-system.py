class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heaps = {}
        self.cache = {}
        
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            item = (-rating, food, cuisine)
            
            if cuisine not in self.heaps:
                self.heaps[cuisine] = []
            
            heapq.heappush(self.heaps[cuisine], item)
            self.cache[food] = item
            
    def changeRating(self, food: str, newRating: int) -> None:
        _, food, cuisine = self.cache[food]
        newItem = (-newRating, food, cuisine)
        self.cache[food] = newItem
        heapq.heappush(self.heaps[cuisine], newItem)

    def highestRated(self, cuisine: str) -> str:
        while self.heaps[cuisine]:
            rating, food, _ = self.heaps[cuisine][0]
            
            if self.cache[food][0] != rating:
                heapq.heappop(self.heaps[cuisine])
                continue
            
            return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)