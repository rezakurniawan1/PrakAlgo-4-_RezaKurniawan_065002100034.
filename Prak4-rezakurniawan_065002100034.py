print("---Program Konversi Bilangan---")
print("""1 -> Desimal ke Biner
2 -> Biner ke Desimal
3 -> Exit""")

while True:
    menu = input("\nSilahkan pilih menu: ")

    if int(menu) == 1:
        desimal = int(input("Masukkan bilangan desimal: "))
        biner = bin(desimal).replace("0b", "")
        print("Nilai binernya adalah: ", biner)

    elif int(menu) == 2:
        biner = input("Masukkan bilangan biner: ")

        desimal = int(biner, 2)
        print("Nilai desimalnya adalah: ", desimal)

    elif int(menu) == 3:
        print("Terimakasih telah menggunakan program ini")
        break