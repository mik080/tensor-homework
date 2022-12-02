#!/usr/bin/python3
import psutil
import datetime
import platform
import time

hostname=platform.node()
mem_ut=psutil.virtual_memory()[3]
time_meas=datetime.datetime.now().timestamp()

time_meas=time.time_ns()

print("memory,host="+str(hostname)+",contur=prod memory_utilization="+str(mem_ut)+" "+str(round(time_meas)))

