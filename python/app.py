import numpy as np

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

def renderScene:
    pixels = np.cartesian(range(SCREEN_WIDTH), range(SCREEN_HEIGHT))
    for pixel_x, pixel_y in pixels:


# flag,
# u, v - barycentric coordinates
# t - distance from the ray origin
def rayTriangleIntersection(o, d, p0, p1, p2):
    epsilon = 0.00001
    e1 = p1-p0
    e2 = p2-p0
    q  = np.cross(d,e2)
    a  = np.dot(e1,q)
    if (np.greater(a, -epsilon) and np.less(a, epsilon)):
        return [False, 0, 0, 0]

    f = 1/a
    s = o-p0
    u = f*np.dot(s,q)

    if (u<0.0): # the intersection is outside of the triangle
        return [False, 0, 0, 0]

    r = np.cross(s,e1)
    v = f*np.dot(d,r)

    if (v<0.0 or u+v>1.0): # the intersection is outside of the triangle
        return [False, 0, 0, 0]

    t = f*np.dot(e2,r); # verified!
    flag = True
    return [flag, u, v, t]

v0 = np.array([-2,-3,0])
v1 = np.array([1,2,0])
v2 = np.array([-7,7,0])
origin = np.array([-2, 2, 1])
direction = -np.array([-4, 2, 2])

print(rayTriangleIntersection(origin, direction, v0, v1, v2))