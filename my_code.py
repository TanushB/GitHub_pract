def calculatePrice(price, tax, discount):
    total_price = price + (price * tax / 100)
    if discount > 0:
        if discount < 10:
            total_price = total_price - (total_price * 0.1)
        else:
            total_price = total_price - (total_price * 0.2)
    return total_price

print(calculatePrice(100, 5, 15))
print(calculatePrice(200, 5, 5))
print(calculatePrice(300, 10, 0))
