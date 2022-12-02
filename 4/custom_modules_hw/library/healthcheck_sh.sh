#!/bin/bash
# WANT_JSON

addr=$(cat $1 | grep -Po '(?<="addr": ")(.*?)(?=")')
tls=$(cat $1 | grep -Po '(?<="tls": )(.*?)(?=,)')

if [ "$tls" == true ]; then
  res=$(curl -sIk https://$addr | grep 'HTTP' | awk '{print $2}')
else
  res=$(curl -sI http://$addr | grep 'HTTP' | awk '{print $2}')
fi

if [ "$res" == "200" ]; then
  msg='Avaible'
else
  msg='Error'
fi
echo "{\"changed\":\"False\", \"rc\":\"$res\", \"msg\":\"Failed\", \"site_status\":\"$msg\"}"