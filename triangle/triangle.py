from enum import Enum

class TriangleType(Enum):
    ACUTE = 'acute'
    RIGHT = 'right'
    OBTUSE = 'obtuse'


class Triangle:
    def __init__(self, sides):
        self.sides = sorted(sides, key=lambda x: -x)

        if self.sides[0] >= self.sides[1] + self.sides[2]:
            raise ValueError('Is not triangle!')

    def get_type(self) -> TriangleType:
        square_big = self.sides[0] * self.sides[0]
        square_small = self.sides[1] * self.sides[1] + self.sides[2] * self.sides[2]
        if square_big == square_small:
            return TriangleType.RIGHT
        elif square_big > square_small:
            return TriangleType.OBTUSE
        else:
            return TriangleType.ACUTE
