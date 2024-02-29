import pickle

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('lista.txt', 'w') as f:
    f.write(str(lista))

with open("lista.txt", "r") as f:
    dane = f.read()

print(dane)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(dane))  # <class 'str'>
print(dane[0])  # [

with open('lista.pickle', 'wb') as f:
    pickle.dump(lista, f)

with open('lista.pickle', 'rb') as f:
    loaded_list = pickle.load(f)

print(loaded_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1

# serializacja
ser_lista = pickle.dumps(lista)  # b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\tK\ne.'
print(ser_lista)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# deserializacja
print(pickle.loads(ser_lista))
