class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def lerp(self, t, vector):
        x = self.x + (vector.x - self.x) * t
        y = self.y + (vector.y - self.y) * t
        z = self.z + (vector.z - self.z) * t
        return Vector(x, y, z)