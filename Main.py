# Imports required modules
import os
import datetime
dt = datetime.datetime.now()
# pulls the month out of the datetime module and sets it to a string variable of month
month = dt.strftime("%b%d")
month = str(month)
# runs tcpdump for 10 packets and writes to logs/log.txt
os.system("tcpdump -i any -c10 > logs/log.txt")
# creates the fileSave function to open the output of the os.system command and then writes it to
# the final log file with the date on it. Then removes the logs/log.txt file for the next os.system commands
def fileSave():
    fOpen = open("logs/log.txt", "r")
    fRead = fOpen.read()
    fWrite = open("logs/%s-log.txt" % month, "a")
    fWrite.write("\n%s" % fRead)
    fWrite.close()
    os.remove("logs/log.txt")

# calls fileSave
fileSave()
# runs iostat and saves to logs/log.txt
os.system("iostat > logs/log.txt")
# calls fileSave
fileSave()
# runs ps and saves to logs/log.txt
os.system("ps > logs/log.txt")
# calls fileSave
fileSave()
# runs uptime and saves to logs/log.txt
os.system("uptime > logs/log.txt")
# calls fileSave
fileSave()
# cats meminfo and saves to logs/log.txt
os.system("cat /proc/meminfo > logs/log.txt")
# calls fileSave
fileSave()
# prints script has finished.
print("System-Monitoring Script has finished.")
