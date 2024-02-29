import requests as req

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = req.get(url)
print(response.status_code)  # 200
print(response)  # <Response [200]>
# 2xx - success
# 3xx - Redirect - przekierowania
# 4xx - Klient np. 404 NOT FOUND, 400 Bad Request, 401 autoryzacja
# 5xx - z serwera

print(response.text)
data = response.json()
print(data)
print(type(data))

print(data.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
print(data['code'])  # USD
print(data['rates'])  # [{'no': '042/A/NBP/2024', 'effectiveDate': '2024-02-28', 'mid': 3.9922}]
print(data['rates'][0]['mid'])  # 3.9922

for k in data.keys():
    print(k)
    print(data[k])
