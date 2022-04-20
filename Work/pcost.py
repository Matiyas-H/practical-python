import csv
f = open("Data/portfolio.csv")
rows = csv.reader(f)
headers = next(f)


def calc_cost(x):
    total_cost = 0
    for row in x:
        stoke_cost = row[2]
        total_cost = total_cost + float(stoke_cost)
    return round(total_cost, 3)


print("total stoke cost: ", calc_cost(rows))
