from ursina import *

def gfloor(floor_texture = '', model_floor = 'block'):
    for a in range(1, 61):
        for b in range(1, 61):
            line1 = Entity(model= model_floor,
                texture = floor_texture,
                collider= 'box',
                position=(a, -8, b))
