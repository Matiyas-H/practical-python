import os

full_path = os.path.expanduser("/Work/Data/portfolio.csv")

with open(full_path) as f:
    data = f.read()


print(data)
