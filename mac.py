import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet chance mach")

print("""
welcome to the chance machine :
1) random
2) static
3) return normal
""")

islemno = raw_input("select the operation: ")
if islemno == "1":
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth0 up")
    print("/033[92m yeni mac adresi atandi.")
elif islemno == "2":
    mac = raw_input("enter the mac address: ")
    os.system("ifconfig eth0 down")
    os.system("macchanger -m " + mac + " eth0")
    os.system("ifconfig eth0 up")
    print("\033[92m yeni mac adresi atandi.")
elif islemno == "3":
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    print("\033[92m mac adresi normal haline getirildi.")
else:
    print("\033[91m hatali islem numarasi girdiniz.")
    print("\033[93m program sonlandiriliyor...")
    exit(1)
