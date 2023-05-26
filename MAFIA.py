import os,platform
os.system('git pull')
 
MAFIA=platform.architecture()[0]
if MAFIA=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif MAFIA=="64bit":
    #print('Command is in update wait we will fix it soon !')
    __import__("MAFIA")
