def currency_converter(usd_val):
    return usd_val * 277.89

usd_val = float(input("Enter USD Amount: "))

pkr_val = currency_converter(usd_val)

print(usd_val, "USD =", pkr_val, "PKR")