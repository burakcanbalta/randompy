import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet vpn control")
print("Welcome to VPN Control")

hedefip = input("Enter the target IP address: ")
os.system("ike-scan " + hedefip)
