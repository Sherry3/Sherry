import os
import time

#f = '/home/sourabh/Desktop/Sherry/log_cpu_freq.txt'
time.sleep(120)

#os.system('sudo echo ------------------------------------------- >> ' + f)
#os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq >> ' + f)
#os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq >> ' + f)

#os.system('sudo ./changeFreq.sh')
os.system('sudo python3 /home/sourabh/Desktop/Sherry/Monitor.py')

#os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq >> ' + f)
#os.system('sudo cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq >> ' + f)
#os.system('sudo echo ------------------------------------------- >> ' + f)

os.system('sudo chmod 777 *.txt')
os.system('sudo chmod 777 */*.txt')

os.system('sudo reboot')
