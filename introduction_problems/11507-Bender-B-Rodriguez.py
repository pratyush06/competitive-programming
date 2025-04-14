def cross(u, v):
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    )

def str_to_vector(s):
    if s == "+y": return (0, 1, 0)
    if s == "-y": return (0, -1, 0)
    if s == "+z": return (0, 0, 1)
    if s == "-z": return (0, 0, -1)
    return (0, 0, 0)

def vector_to_str(v):
    lookup = {
        (1, 0, 0): "+x",
        (-1, 0, 0): "-x",
        (0, 1, 0): "+y",
        (0, -1, 0): "-y",
        (0, 0, 1): "+z",
        (0, 0, -1): "-z",
    }
    return lookup[v]

while True:
    L = int(input())
    if L == 0:
        break
    decisions = input().split()
    direction = (1, 0, 0)  # starts at +x

    for d in decisions:
        if d == "No":
            continue
        rotated = str_to_vector(d)
        axis = cross((1, 0, 0), rotated)
        new_dir = cross(axis, direction)
        if new_dir != (0, 0, 0):
            direction = new_dir

    print(vector_to_str(direction))
