import os
time = input('The system will be shutdown after XX seconds: ')
command = r'shutdown /s /t %s' % time
os.system(command)
