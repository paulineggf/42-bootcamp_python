from vector import Vector


vector = Vector([0.0, 0.23, 0.54])
vector2 = Vector(3)
vector3 = Vector((1, 3))
print (vector.values)
print (vector.size)
print (vector2.values)
print (vector2.size)
print (vector3.values)
print (vector3.size)

vector4 = vector + 2

print (vector4.values)
print (vector4.size)

vector5 = 2 + vector

print (vector5.values)
print (vector5.size)

vector6 = vector - 2

print (vector6.values)
print (vector6.size)

vector7 = 2 - vector

print (vector7.values)
print (vector7.size)


vector8 = 2 / vector

print (vector8.values)
print (vector8.size)

print (str(vector))

print (repr(vector))
