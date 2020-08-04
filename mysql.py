import MySQLdb
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


def my_quit_fn():
    os.system('clear')
    raise SystemExit


def invalid():
   print "INVALID CHOICE!"
   os.system('clear')

def my_updateupgrade_fn():
	os.system('clear')
	os.system('xterm -e apt-get upgrade && upgrade')
	main()


def linuxgsm():
    os.system('clear')
    if os.path.isdir('LinuxGSM-Docs'):
        print ""
        install_modules()
    else:
         print('\033[5m\033[1m\033[31mINSTALLATION\033[0m')
         os.system('https://github.com/GameServerManagers/LinuxGSM-Docs.git')
         os.system('clear')

def install_modules():
    answ=True
    while answ:
        print("""
         1.Linux-GSM (game server manager)
         2.Install
         3.Install
         4.
         5.
         6.CREDITS
         7.I REALY REALY love BITCOIN AND MONERO
         00.Exit/Quit
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
            linuxgsm()
        # elif ans=="2":
        # elif ans=="6":
        # elif ans=="4":

        elif ans=="00":
          my_quit_fn()
          ans = None
        else:
            os.system('clear')
            print("\n Not Valid Choice Try again")
            time.sleep(0.5)
            os.system('clear')


def main():
    answ=True
    while answ:
        print("""
         1.Install modules
         2.Install Panels
         3.Install Games servers
         4.
         5.
         6.CREDITS
         7.I REALY REALY love BITCOIN AND MONERO
         00.Exit/Quit
         """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
            install_modules()
        elif ans=="2":
            install_panels()
        elif ans=="6":
            credits()

        # elif ans=="4":

        elif ans=="00":
          my_quit_fn()
          ans = None
        else:
            os.system('clear')
            print("\n Not Valid Choice Try again")
            time.sleep(0.5)
            os.system('clear')




# --------------------------------MAIN---------------------------------------------------------
# ----------------------------------------------------------------------------------------------


if __name__ == "__main__":
	main()



























# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                      user="root",         # your username
#                      passwd="megajonhy",  # your password
#                      db="jonhydb")        # name of the data base
#
# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()
#
# # Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")
#
# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[0]
#
# db.close()
