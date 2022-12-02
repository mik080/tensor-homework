#!/usr/bin/python3
import psutil
import datetime
import platform
import time

hostname=platform.node()
cpu_ut=psutil.cpu_percent(interval=3)
time_meas=datetime.datetime.now().timestamp()
time_meas=time.time_ns()

print("cpu_ut,host="+str(hostname)+",contur=prod cpu_utilization="+str(cpu_ut)+" "+str(round(time_meas)))


