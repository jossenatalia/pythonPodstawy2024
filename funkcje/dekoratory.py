# @ dekorator
# działają na zasadzie funkcji wewnętrznej

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew  # adres funkcji


@dekor
def hey():
    print("Hello")


@dekor
def dodawanie():
    print(1 + 2)


hey()
dodawanie()
