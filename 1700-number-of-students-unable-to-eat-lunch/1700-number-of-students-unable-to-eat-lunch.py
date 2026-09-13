from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=deque(students)
        sandwiches=deque(sandwiches)
        rotation=0
        while sandwiches and rotation < len(students):
            x=students.popleft()
            if x == sandwiches[0]:
                sandwiches.popleft()
                rotation=0
            else:
                students.append(x)
                rotation+=1 
                  
        return len(students)        