#M Gigih Lanang P
#NIM  : 20051397053
#Prodi: D4 Manajemen Informatika (2020A)

desimal = int(input('Masukkan Bilangan Desimal = '))

biner = bin(desimal) .replace("0b","")
oktal = oct(desimal) .replace("0o","")
hexa = hex(desimal) .replace("0x","")
print(biner,oktal,hexa)
