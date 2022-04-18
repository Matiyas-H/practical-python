height = 100
no_bounce = 1

for i, v in enumerate(range(1, 11), start=1):
    while no_bounce <= v:
        height = height * 3/5
        print(i, round(height, 4))
        break
