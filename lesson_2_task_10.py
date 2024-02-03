def bank(X, Y):
    amount = X * (1 + 0.14)**Y
    return amount
x = float(input("What amount would you like to deposit? "))
y = int(input("How many years would you like to keep your investment for? "))

initial_deposit = x
years = y
result = bank(initial_deposit, years)
print(f"Сумма на счету через", years, "лет будет:", result)
