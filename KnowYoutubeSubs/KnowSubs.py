import subprocess
import sys
import time

time.sleep(12) 
p = subprocess.Popen(['powershell.exe', 'C:\\Users\\divya\\OneDrive\\Desktop\\KnowYoutubeSubs\\SubscribersSpeak.ps1'], stdout=sys.stdout)
p.communicate()