class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        while asteroids:
            newAsteroids = []
            isDifferent = False
            
            while asteroids:
                curr = asteroids.pop(0)
                
                if not newAsteroids:
                    newAsteroids.append(curr)
                else:
                    if (curr < 0 and newAsteroids[-1] > 0):
                        prev = newAsteroids.pop()
                        if -curr < prev:
                            newAsteroids.append(prev)
                        elif -curr > prev:
                            newAsteroids.append(curr)
                        isDifferent = True
                    else:
                        newAsteroids.append(curr)
             
            if not isDifferent:
                break
            asteroids = newAsteroids

            
        return newAsteroids