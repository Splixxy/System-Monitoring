import os
import datetime
dt = datetime.datetime.now()
month = dt.strftime("%b%d")
month = str(month)
os.system("tcpdump -i any -c10 > logs/log.txt")

def fileSave():
    fOpen = open("logs/log.txt", "r")
    fRead = fOpen.read()
    fWrite = open("logs/%s-log.txt" % month, "a")
    fWrite.write("\n%s" % fRead)
    fWrite.close()
    os.remove("logs/log.txt")

fileSave()

os.system("iostat > logs/log.txt")
fileSave()

os.system("ps > logs/log.txt")
fileSave()

os.system("uptime > logs/log.txt")
fileSave()

os.system("cat /proc/meminfo > logs/log.txt")
fileSave()

print("System-Monitoring Script has finished.")
