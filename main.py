from view.view_nilai import Cari,cetak
from view.input_nilai import inputan,edit,delete

while True:
    print("\nMenu :","\n(t)ambah (u)bah (h)apus (c)ari (l)ihat (k)eluar")
    c = input("\nPilih Opsi: ")

    if c.lower() == 'k':
        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:
            break
    elif c.lower() == 'l':
        cetak()
    elif c.lower() == 't':
        inputan()
    elif c.lower() == 'u':
        edit()
    elif c.lower() == 'c':
        Cari()
    elif c.lower() == 'h':
        delete()
    else:
        ()