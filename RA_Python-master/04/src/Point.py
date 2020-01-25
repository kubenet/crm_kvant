from math import *


class Point:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def to_vector(self) -> tuple:
        return self.x, self.y, self.z

    def to_json(self) -> str:
        import json
        return json.dumps({
            'x': self.x,
            'y': self.y,
            'z': self.z,
        })

    def distance_to(self, other) -> float:
        return sqrt(
            (other.x - self.x) ** 2 +
            ((other.y - self.y) ** 2) +
            ((other.z - self.z) ** 2)
        )


p = Point(x=0.9, y=5, z=0.0)
print(p.distance_to(Point(-98.8, 7, 0)))
print(p.to_vector())
print(p.to_vector)
print(p.to_json())
