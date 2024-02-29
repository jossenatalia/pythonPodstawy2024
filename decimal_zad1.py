# decimal - biblioteka do działania na precyzyjnych liczbach zmiennoprzecinkowych
import decimal
from decimal import Decimal, getcontext

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.5')
print(kwota1 + kwota2)  # 15.75

precyzja = Decimal('0.00')

roznica = kwota1 - kwota2
print(roznica)  # 4.75
print(roznica.quantize(precyzja))  # 4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem: ", kwota_z_podatkiem)
print("Kwota z podatkiem: ", kwota_z_podatkiem.quantize(precyzja))

getcontext().prec = 2
a = Decimal('1.25685')
b = Decimal('1.78569')
c = a + b
print(c)

d = Decimal('130.75858')
e = a + d
print(e)
