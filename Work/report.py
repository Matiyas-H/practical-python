import csv
from traceback import print_tb
f = open("Data/portfolio.csv")
rows = csv.reader(f)
headers = next(rows)


# sets

portfolio = []


def read_portfolio(filename):
    for row in filename:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)
    return portfolio


def calc_total(lst):
    total = 0
    for name, shares, price in lst:
        total += shares * price
    return total


read_portfolio(rows)
print("total stoke cost is", calc_total(portfolio))
