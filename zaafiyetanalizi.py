import os
os.system("apt-get install figlet")
os.system("clear")
os.system("ZAAFİYET ANALİZİ")
print("""
ZAAFİYET ANALİZİ ARACINA HOSGELDİNİZ""")
hedefip = raw_input("Hedef IP Adresini Giriniz: ")
os.system("nikto -h " + hedefip)
