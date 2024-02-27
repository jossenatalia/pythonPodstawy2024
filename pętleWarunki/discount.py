from datetime import datetime, timedelta, date

today = date.today()
print(today)  # dzisiejsza data
print(type(today))  # <class 'datetime.date'>

time_now = datetime.now()
print(time_now)  # obecny czas
print(type(time_now))  #<class 'datetime.datetime'>

tomorrow = today + timedelta(days=1)
print(tomorrow)

next_time = time_now + timedelta(hours=3)
print(next_time)

print(time_now.time())
print(today.day)

formatted_date = datetime.now().strftime('%d/%m/%Y')
print(formatted_date)

formatted_time = datetime.now().strftime('%H:%M:%S')
print(formatted_time)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 200},
    {'sku': 4, 'exp_date': today, 'price': 500.00},
]

for product in products:
    # print(product)
    if product['exp_date'] != today:
        continue  # weż kolejny element z listy
    product['price'] *= 0.8

    print(f"""
    Price for sku {product['sku']}
    is now {product['price']}
    """)

