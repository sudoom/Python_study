class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        if type(self) == type(other):
            xsum = self.x + other.x
            ysum = self.y + other.y
            return (xsum, ysum)
        else:
            print('something goes wrong')

    def __mul__(self, other):
        if type(self) == type(other):
            xmul = self.x * other.x
            ymul = self.y * other.y
            return(xmul, ymul)
        elif type(other) == int:
            xmul = self.x * other
            ymul = self.y * other
            return(xmul, ymul)
        else:
            print('go wrong')

    def __sub__(self, other):
        if type(self) == type(other):
            xsub = self.x - other.x
            ysub = self.y - other.y
            return(xsub, ysub)
        else:
            print('Wrong')


v1 = Vector(5, 6)
v2 = Vector(2, 7)
print('subtract:', v1-v2)
print('equal:', v1 == v2)
print('summary:', v1+v2)
print('multiply:', v1*v2)
print('multiply:', v1*5)
