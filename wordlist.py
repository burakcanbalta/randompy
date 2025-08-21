import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet wordlist")
print("This script will create a wordlist for you.")

minimum = raw_input("Enter the minimum length of the words: ")
maximum = raw_input("Enter the maximum length of the words: ")
karakter = raw input("Enter the characters : ")
kayıtyeri = raw_input("Enter the save location (e.g., /root/wordlist.txt): ")

os.system("crunch " + minimum + " " + maximum + " " + karakter + " -o " + kayıtyeri)
print("Wordlist created successfully at " + kayıtyeri)
