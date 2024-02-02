def bank(X, Y):
    amount = X * (1 + 0.10)**Y
    return amount
initial_deposit = 100000
years = 10
result = bank(initial_deposit, years)
print("Сумма на счету через", years, "лет будет:", result)