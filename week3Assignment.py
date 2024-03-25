def calculate_discount(price,discount_percent):
    if discount_percent>=20:
        final_price=price-price*(discount_percent/100)
        print('The final price is:', final_price)
    else:
        print('The original price is:',price)
calculate_discount(500,30)

price=float(input('Enter the price of an item:'))
discount_percent=float(input("Enter the discount percent:"))
calculate_discount(price,discount_percent)