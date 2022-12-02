#!/usr/bin/env python3
from prometheus_client import start_http_server, Summary, Gauge
import random
import time

from  kubernetes import client , config 

config.load_incluster_config()
#config.load_kube_config()
v1= client.CoreV1Api()

# for i in ret_pod.items:
#     print(i.metadata.name)

# Create a metric to track time spent and requests made.

COUNT_PODS=Gauge('count_pods', 'Count pods in cluster')

# Decorate function with metric.
# @COUNT_PODS.time()
# def pods_request(t):
#     """A dummy function that takes some time."""
#     time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9100)
    COUNT_PODS.set_to_current_time() 
    # Generate some requests.
    while True:
        ret_pod = v1.list_pod_for_all_namespaces(watch=False)
        pods=(len(ret_pod.items))
        COUNT_PODS.set(pods)
        time.sleep(3)