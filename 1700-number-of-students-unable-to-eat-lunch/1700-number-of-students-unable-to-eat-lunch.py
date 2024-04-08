class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        square = 0
        circle = 0
        for student in students:
            if student == 0:
                circle += 1
                continue
            square += 1
        
        for sandwich in sandwiches:
            if sandwich == 0 and circle == 0:
                return square
            if sandwich == 1 and square == 0:
                return circle
            
            if sandwich == 0:
                circle -= 1
                continue
            square -= 1
        
            
        return 0