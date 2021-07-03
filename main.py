# -*- coding: utf-8 -*-

import time
import diff
import ssh
import log_replace
import os
from pyfiglet import Figlet

#ssh
device_path = "input/device"

device_file = os.listdir(device_path)
device_files = [f for f in device_file if os.path.isfile(os.path.join(device_path, f))]
print(device_files)

for dev in device_files:
    ssh.ssh_log(dev)


#logリプレース
log_path = "input/log"

log_file = os.listdir(log_path)
log_files = [f for f in log_file if os.path.isfile(os.path.join(log_path, f))]
print(log_files)

for log in log_files:
    log_replace.replace(log)

print("-----------------------------")

#diff
for log in log_files:
    diff.diff_log(log)

#finish
f = Figlet(font="slant")
msg = f.renderText("FINISH !")
print(msg)

