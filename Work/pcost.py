import csv

f = open("Data/portfolio.csv")
rows = csv.reader(f)
headers = next(f)


def calc_cost(x):
    total_cost = 0
    for row in x:
        no_share = int(row[1])
        share_cost = float(row[2])
        total_cost += no_share * share_cost

    return total_cost


print("total cost: ", calc_cost(rows))
