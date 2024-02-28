def connect(**opcje):  # ** argumenty słownikowe
    print(opcje)
    connect_params = {'host': '127.0.0.7', 'port': '8080', 'pwd': opcje}
    print(connect_params)


def all_args(*args, **opcje):
    print(args, opcje)


connect(opcje=(1, 2, 3), opcje2=4, opcje3=5)
connect(name="Radek", age=20, city="Krakow")
