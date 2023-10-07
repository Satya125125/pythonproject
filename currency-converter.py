import requests

from_currency = str(input("Enter the currency you want to change from: ")).upper()

to_currency = str(input("Enter the cuuency you want to change to: ")).upper()

amount = float(input("Enter the amoynt to be converted: "))

access = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"{amount} {from_currency} is {access.json() ['rates'] [to_currency]} {to_currency}")
