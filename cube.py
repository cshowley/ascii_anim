import math
import time
import os

def rotate_3d(vertex, theta, phi):
    x, y, z = vertex
    # Rotate around X axis
    new_y = y * math.cos(theta) - z * math.sin(theta)
    new_z = y * math.sin(theta) + z * math.cos(theta)
    y, z = new_y, new_z
    # Rotate around Y axis
    new_x = x * math.cos(phi) + z * math.sin(phi)
    new_z = -x * math.sin(phi) + z * math.cos(phi)
    x, z = new_x, new_z
    return (x, y, z)

def project_3d_to_2d(vertex, scale=20):
    x, y, z = vertex
    factor = scale / (z + scale + 3)
    return (
        int(x * factor * 10 + 40),
        int(y * factor * 8 + 12)
    )

# Initialize cube vertices
vertices = [(x, y, z) for x in [-1.2, 1.2] for y in [-1, 1] for z in [-1, 1]]
edges = [(i, j) for i in range(8) for j in range(i+1, 8) if bin(i ^ j).count('1') == 1]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    screen = [[' ' for _ in range(80)] for _ in range(24)]
    
    # Rotate and project vertices
    projected = []
    for v in vertices:
        rotated = rotate_3d(v, time.time(), time.time() * 0.5)
        projected.append(project_3d_to_2d(rotated))
    
    # Draw edges with division safety
    for i, j in edges:
        x1, y1 = projected[i]
        x2, y2 = projected[j]
        dx, dy = x2 - x1, y2 - y1
        steps = max(abs(dx), abs(dy))
        
        if steps == 0:
            if 0 <= y1 < 24 and 0 <= x1 < 80:
                screen[y1][x1] = '#'
        else:
            for k in range(steps + 1):
                x = x1 + dx * k // steps
                y = y1 + dy * k // steps
                if 0 <= y < 24 and 0 <= x < 80:
                    screen[y][x] = '#'
    
    print('\n'.join(''.join(row) for row in screen))
    time.sleep(0.05)
