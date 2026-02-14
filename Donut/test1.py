import math

r = 10

for theta in [i * 0.1 for i in range(63)]:  # 0 → 2π
    x = int(r * math.cos(theta))
    y = int(r * math.sin(theta))
    print(" " * (x + 15) + "*")
