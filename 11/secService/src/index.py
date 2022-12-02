#!/usr/bin/env python3
import requests
import time,os, datetime
import concurrent.futures


url=os.environ['url']

etimeout=5
if __name__ == '__main__':
    
    
    while True:
        
        try:
            timeout=5
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=35) as executor:
                
                while True:
                    future_list = set()
                    while True:
                        future = executor.submit(requests.get, url)
                        future_list.add(future)
                        
                        budget = timeout
                        previous = datetime.datetime.now()
                        while budget > 0:
                            try:
                                for future in concurrent.futures.as_completed(future_list, budget):
                                    budget -= ( datetime.datetime.now()- previous ).total_seconds()
                                    response = future.result()
                                    print(response.text)
                                    if response.status_code==200:
                                        etimeout=5
                                    future_list.remove(future)
                            except concurrent.futures.TimeoutError:
                               
                                budget -= (datetime.datetime.now()-previous ).total_seconds()
                                
      
        
        except requests.exceptions.ConnectionError:
            etimeout=etimeout*2
            if etimeout>180:
                etimeout=180
            time.sleep(etimeout)
            cur_time=datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"{cur_time} connection lost {etimeout=}")
