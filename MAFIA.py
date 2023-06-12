import os,platform
os.system('git pull')
 
MAFIA=platform.architecture()[0]
if MAFIA=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif MAFIA=="64bit":
     __import__("Muzammil")


