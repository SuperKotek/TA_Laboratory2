import math

class __math_func__():

    def paral_volume_func(x, y, z):
        V = x*y*z
        return round(V, 6)

    def paral_squaresurf_func(x, y, z):
        S = 2 * (x * y + x * z + y * z)
        return round(S, 6)

    def tetra_volume_func(a):
        V = math.pow(a, 3) / (6 * math.sqrt(2))
        return round(V, 6)

    def tetra_squaresurf_func(a):
        S = math.sqrt(3) * math.pow(a, 2)
        return round(S, 6)

    def orb_volume_func(r):
        V = (4 * math.pi * math.pow(r, 3)) / 3
        return round(V, 6)

    def orb_squaresurf_func(r):
        S = 4 * math.pi * math.pow(r, 2)
        return round(S, 6)

    def mass_func(p, v):
        mass = p * v
        return round(mass, 6)