import os
time = int(input('The system will be shutdown after XX minutes: ')) * 60
command = r'shutdown /s /t %s' % time
os.system(command)