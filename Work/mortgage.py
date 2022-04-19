loan_amount = 500000.0
rate = 0.05
monthly_payment = 2684.11
month = 0
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment_amount = 1000


while loan_amount > 0:
    month = month + 1
    loan_amount = loan_amount * (1+rate/12) - monthly_payment
    total_paid += monthly_payment
    if monthly_payment >= extra_payment_start_month and monthly_payment <= extra_payment_end_month:
        loan_amount -= extra_payment_amount
        total_paid += extra_payment_amount
    print(monthly_payment, round(total_paid, 3), round(loan_amount, 2))

print("Total paid", total_paid)
print("months", month)
