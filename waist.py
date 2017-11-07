#하나의 포인트를 찾고 그 포인트에 대해서 upper와 lower을 찾는다.

# position of single point
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class FindArea:
    def __init__(self,UpperLimit, LowerLimit):
        self.UpperLimit = UpperLimit
        self.LowerLimit = LowerLimit

