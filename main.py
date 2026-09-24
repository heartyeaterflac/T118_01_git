def lunch_total(price, quantity):
    lunch_price = price * quantity
    if lunch_price >= 3000:
        return lunch_price - 300
    else:
        return lunch_price

print("EKEB, стоимость:", lunch_total(1200, 3))