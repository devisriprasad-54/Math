import math

R = 2
r = 1

points = []

for theta in [i * 0.3 for i in range(20)]:
    for phi in [i * 0.3 for i in range(20)]:
        
        x = (R + r * math.cos(theta)) * math.cos(phi)
        y = (R + r * math.cos(theta)) * math.sin(phi)
        z = r * math.sin(theta)
        
        points.append((x, y, z))

print(points[:5])
