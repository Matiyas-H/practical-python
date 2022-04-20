f = open("Data/portfolio.csv")

# headers = next(f)

for line in f:
    data = line["price"]
    print(data)
