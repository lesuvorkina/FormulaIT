# TODO Найдите количество книг, которое можно разместить на дискете
lines_on_the_page = int(input("Введите количество строк на странице: "))
Pages = int(input ("введите количество страниц в книге: "))
symbols = int(input("введите количество символов в строке: "))
weigh_of_symbol = float(input ("Введите вес одного символа (в байтах): "))
DiskVolume = float(input("Введите объём диска в Мб: "))
DiskVolume=DiskVolume*(1024**2)
print("на диске поместится "+ str(DiskVolume//(Pages * lines_on_the_page * symbols * weigh_of_symbol))+" книг")
