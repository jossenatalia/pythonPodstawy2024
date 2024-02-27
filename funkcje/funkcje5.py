# stworzyć funkcję kantor
# dwie funkcje wewnętrzned eur, usd
# w zależności od waluty ma nam zwracać odpowiednią funkcję
# funkcje wewnętrzne będą przeliczać tylko 1 typ waluty według ich nazwy

def kantor(waluta):
    def eur(kwota=0):
        print(int(kwota * 4.4))

    def usd(kwota=0):
        print(int(kwota * 4.2))

    if waluta == 'euro':
        return eur
    else:
        return usd


kantor_eur = kantor('euro')
kantor_eur(500)

kantor_usd = kantor('usd')
kantor_usd(500)

