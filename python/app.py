import numpy as np
from PIL import Image
import pdb

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
light_point = np.array([7,3,10])
camera = np.array([7,0,0])
objects = [
    np.array([0.5,0,0]),
    np.array([0,0.5,0]),
    np.array([0,0,0.5])
]

def renderScene():
    data = np.zeros( (SCREEN_WIDTH,SCREEN_HEIGHT,3), dtype=np.uint8 )
    for pixel_x in range(SCREEN_WIDTH):
        for pixel_y in range(SCREEN_HEIGHT):
            data[pixel_x, pixel_y] = calculatePixel(pixel_x, pixel_y)
    image = Image.fromarray(data)
    image.show()

def calculatePixel(x, y):
    primary_ray = np.array([camera[0]-1, camera[1], camera[2]])
    closest_intersection = None
    for object in objects:
        intersec = rayTriangleIntersection(camera, primary_ray, objects[0], objects[1], objects[2])
        if (not closest_intersection or closest_intersection[3] < intersec[3]): closest_intersection = intersec
    color = [255, 0, 0] if closest_intersection else [255, 255, 255]
    return color

def parseObjects(filename):
    # ...

# Response [flag, u, v, t]
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

# v0 = np.array([-2,-3,0])
# v1 = np.array([1,2,0])
# v2 = np.array([-7,7,0])
# origin = np.array([-2, 2, 1])
# direction = -np.array([-4, 2, 2])
#
# print(rayTriangleIntersection(origin, direction, v0, v1, v2))
renderScene()