class vector:
    x = 0
    y = 0
    z = 0
def vector_components():
    v = vector()
    v.x = 2
    v.y = 4
    v.z = 6
    print("Components of Vectors are:", v.x, v.y, v.z)
vector_components()
def reverse_vectors():
    v = vector()
    v.x = 2
    v.y = 4
    v.z = 6
    print("Components of Reverse Vectors are:", -v.x, -v.y, -v.z)
reverse_vectors()
def add_vectors():
    v1 = vector()
    v1.x = 2
    v1.y = 4
    v1.z = 6
    v2 = vector()
    v2.x = 2
    v2.y = 4
    v2.z = 6
    x = v1.x + v2.x
    y = v1.y + v2.y
    z = v1.z + v2.z
    vec = x,y,z
    print("Sum of two vectors are:", vec)
add_vectors()
def dot_product():
    v1 = vector()
    v1.x = 2
    v1.y = 4
    v1.z = 6
    v2 = vector()
    v2.x = 2
    v2.y = 4
    v2.z = 6
    x = v1.x * v2.x
    y = v1.y * v2.y
    z = v1.z * v2.z
    vec = x + y + z
    print("Dot product of two vectors are:", vec)
dot_product()
def cross_vector():
    v1 = vector()
    v1.x = 2
    v1.y = 4
    v1.z = 6
    v2 = vector()
    v2.x = 3
    v2.y = 5
    v2.z = 7
    vx = (v1.y * v2.z) - (v1.z * v2.y)
    vy = (v1.z * v2.x) - (v1.x * v2.z)
    vz = (v1.x * v2.y) - (v1.y * v2.x)
    vec = vx, vy, vz
    print("Cross Product of two vector are:", vec)
cross_vector()
def magnitude():
    v = vector()
    v.x = 2
    v.y = 4
    v.z = 6
    vect = ((v.x ** 2) + (v.y ** 2) + (v.z ** 2)) ** (1/2)
    print("Magnitude of a vector is:", vect)
magnitude()


