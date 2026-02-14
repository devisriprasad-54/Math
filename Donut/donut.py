import math
import os
import time

width = 80
height = 40

R = 2
r = 1

A = 0
B = 0

while True:
    zbuffer = [0] * (width * height)
    screen = [" "] * (width * height)

    for theta in [i * 0.07 for i in range(90)]:
        for phi in [i * 0.02 for i in range(314)]:

            x = (R + r * math.cos(theta)) * math.cos(phi)
            y = (R + r * math.cos(theta)) * math.sin(phi)
            z = r * math.sin(theta)

            # rotation
            x1 = x * math.cos(B) - y * math.sin(B)
            y1 = x * math.sin(B) + y * math.cos(B)
            z1 = z

            y2 = y1 * math.cos(A) - z1 * math.sin(A)
            z2 = y1 * math.sin(A) + z1 * math.cos(A)

            # projection
            ooz = 1 / (z2 + 5)
            xp = int(width/2 + 30 * ooz * x1)
            yp = int(height/2 - 15 * ooz * y2)

            idx = xp + yp * width

            if 0 <= idx < width * height:
                if ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    screen[idx] = ".,-~:;=!*#$@"[int(ooz * 8)]

    os.system("cls" if os.name == "nt" else "clear")
    output = ""
    for i in range(0, width * height, width):
        output += "".join(screen[i:i+width]) + "\n"
    print(output)


    A += 0.04
    B += 0.02
    time.sleep(0.03)
