# single assignment
x = 10
message = "Hello, Python!"
pi_approx = 3.14

print(x, message, pi_approx)

# multiple assignment (same value)
a = b = 0

# multiple assignment (different values) and unpacking
x, y, z = 1, 2, 3

v = 5
print(v, type(v))   # int
v = "now a string"
print(v, type(v))   # str

i = 42           # int
f = 3.1415       # float
c = 1 + 2j       # complex

print(i, f, c)
print(type(i), type(f), type(c))


t = True
f = False
print(t, f, type(t)) 
print("Truth of 0:", bool(0), "Truth of non-empty string:", bool("hi"))