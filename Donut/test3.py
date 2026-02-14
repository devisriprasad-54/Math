import math
import os

R = 2
r = 1
k = 5

while True:
    os.system("cls" if os.name == "nt" else "clear")
    
    screen = [[" "]*80 for _ in range(24)]
    
    for theta in [i * 0.3 for i in range(20)]:
        for phi in [i * 0.3 for i in range(20)]:
            
            x = (R + r * math.cos(theta)) * math.cos(phi)
            y = (R + r * math.cos(theta)) * math.sin(phi)
            z = r * math.sin(theta)
            
            xp = int(40 + 20 * x/(z+k))
            yp = int(12 + 20 * y/(z+k))
            
            if 0 <= xp < 80 and 0 <= yp < 24:
                screen[yp][xp] = "*"
    
    for row in screen:
        print("".join(row))
