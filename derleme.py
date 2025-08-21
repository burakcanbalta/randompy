import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet derleme aracı")
print("Derleme aracı çalıştırılıyor...")

derle = raw_input("Programın adını girin: ")
py_compile.compile(derle)
