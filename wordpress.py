import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet hoşgeldiniz")
print("""
1) hızlı tarama
2) eklentili tarama
3) tema tarama
4) yönetici kullanıcı adı tarama
""")

islemno = raw_input("işlem numarasını giriniz: ")

if islemno == "1":
    site = raw_input("site adresini giriniz: ")
    os.system("wpscan --url " + site)
elif islemno == "2":
    site = raw_input("site adresini giriniz: ")
    os.system("wpscan --url " + site + " --enumerate p")
elif islemno == "3":
    site = raw_input("site adresini giriniz: ")
    os.system("wpscan --url " + site + " --enumerate t")
elif islemno == "4":
    site = raw_input("site adresini giriniz: ")
    os.system("wpscan --url " + site + " --enumerate u")
else:
    print("Geçersiz işlem numarası. Lütfen 1, 2, 3 veya 4 giriniz.")
    exit(1)
