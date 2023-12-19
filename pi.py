import decimal

decimal.getcontext().prec = 13  # One extra decimal place for rounding

# Calculate pi with the desired precision
pi_value = decimal.Decimal(22) / decimal.Decimal(7)

# Print the value of pi
print(f"The value of pi with precision up to 12 decimal places: {pi_value}")