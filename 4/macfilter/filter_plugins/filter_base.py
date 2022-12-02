#!/usr/bin/python
import re
from ansible.errors import (
    AnsibleFilterTypeError,
    AnsibleFilterError
)

def mac_filter(mac_str):
    '''
        generate mac address from string
    '''    
    str_lenght= len(mac_str)
    mac_str=':'.join(mac_str[i:i+2] for i in range(0, str_lenght, 2))

    if bool(re.match(r"^[:A-Fa-f0-9]+$", mac_str))==False:
        raise AnsibleFilterError("mac string content wrong char")
    if len(mac_str.replace(":","")) % 2 != 0:
        raise AnsibleFilterError("count char in string not right")
        
    
    
    return mac_str


class FilterModule(object):
    def filters(self):
        return {
            'mac_filter': mac_filter
        }
